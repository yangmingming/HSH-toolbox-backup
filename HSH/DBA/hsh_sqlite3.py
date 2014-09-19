##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-07

'''Usage
from HSH.DBA.hsh_sqlite3 import Database_schema, iterC, prt_all
'''
import sqlite3
import os

class Table(object):
    def __init__(self, name):
        self.name = name
        self.columns = list()
        self.amount = 0
        
    def __str__(self):
        tableinfo = 'table name = %s, column number = %s, entry number = %s\n' \
                    % (self.name, len(self.columns), self.amount)
        columnsinfo = ['{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}'.format(('cID', ##字符美化输出
                                                                                             'COLUMN NAME',
                                                                                             'TYPE',
                                                                                             'NOT NULL',
                                                                                             'dflt_value',
                                                                                             'IS PRIMARY KEY'))]
        for column in self.columns:
            columnsinfo.append('{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}'.format(column))
        return '=========================== TABLE info ============================\n' + \
            tableinfo + '\n'.join(columnsinfo)
            
class Database_schema(object): # sqlite3 database schema object
    def __init__(self, dbpath):
        if not os.path.exists(dbpath):
            raise 'ERROR! database path not exists!!'
        name, _ = os.path.splitext(os.path.basename(dbpath) ) ## 拆分文件名，得到数据库名
        self.name = name 
        self.tables = dict()
        conn = sqlite3.connect(dbpath) ## 连接数据库
        crs = conn.cursor() ## 创建游标
        ## >> 获得数据中所有表的名字 << ##
        crs.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for tablename in crs.fetchall(): ## 给db信息中添加table的信息
            table = Table(tablename[0]) ## 根据表名称，创建表对象
            ## >> 不经过SELECT *, 得到表中所有列的属性细节 << ##
            crs.execute("PRAGMA table_info(%s)" % tablename[0] ) ## 取得列信息
            for info in crs.fetchall(): ## 填写 table.columns
                table.columns.append((str(info[0]), 
                                      str(info[1]), 
                                      str(info[2]), 
                                      str(info[3]), 
                                      str(info[4]), 
                                      str(info[5]))  )
            crs.execute("SELECT count(*) FROM (SELECT * FROM %s);" % tablename[0] ) ## 快速得到表中数据条数
            table.amount = crs.fetchone()[0] ## 填写 table.amount
            self.tables[tablename[0]] = table
            
    def __str__(self):
        return '========================== DATABASE info ==========================\ndatabase name = "' \
        + self.name + '"\n=== list of table name ===\n' + '\n'.join(self.tables)

    def __getattr__(self, item):
        if item not in ['name', 'tables']:
            return self.tables[item]

def iterC(cursor, arraysize = 10):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result
            
def prt_all(c):
    counter = 0
    for row in iterC(c):
        print row
        counter += 1
    print 'Found %s records' % counter

def stable_insertmany(connect, cursor, sqlcmd, records):
    '''INSERT INTO tablename VALUES (%s, %s, ...)
    Skip all the error record
    '''
    try:
        cursor.executemany(sqlcmd, records)
    except: # failed to batch insert, try normal iteratively insert
        for record in records:
            try:
                cursor.execute(sqlcmd, record )
            except:
                pass
    connect.commit()

def unit_test1():
    '''测试database_schema的功能
    '''
    try:
        conn = sqlite3.connect("records.db")
        c = conn.cursor()
        c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, name TEXT, enroll_date DATE)")
        c.execute("INSERT INTO test (id, name, enroll_date) VALUES (?, ?, ?)", (1, "Jack", date(2014,8,15)))
        conn.commit()
        conn.close()
    except:
        print "Something Wrong, please delete 'records.db' then proceed"
    
    db_schema = Database_schema("records.db")
    print db_schema
    print db_schema.test

def unit_test2():
    '''测试stable_insertmany的功能
    '''
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, number INTEGER)")
    records = [(1, 10), (3, 10), (5, 10)] # insert some records at begin
    c.executemany("INSERT INTO test VALUES (?, ?)", records)
    
    records = [(2, 10), (3, 10), (4, 10)]
    stable_insertmany(conn, c, "INSERT INTO test VALUES (?, ?)", records)
    c.execute("SELECT * FROM test")
    for row in c.fetchall():
        print row
        
if __name__ == "__main__":
#     unit_test1()
    unit_test2()
    