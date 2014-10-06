##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-06

"""
from HSH.DBA.hsh_postgres import iterC, prt_all
"""
import psycopg2

def iterC(cursor, arraysize = 10):
    "An iterator that uses fetchmany to keep memory usage down"
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result
            
def prt_all(cursor):
    counter = 0
    for row in iterC(cursor):
        print row
        counter += 1
    print "Found %s records" % counter
    
def stable_insertmany(connect, cursor, sqlcmd, records):
    """INSERT INTO tablename VALUES (%s, %s, ...)
    Skip all the error record
    """
    try:
        c.executemany(cmd, records)
    except psycopg2.IntegrityError:
        conn.rollback() # rollback, then insert one by one
        for record in records:
            try:
                c.execute(cmd, record)
            except psycopg2.IntegrityError:
                conn.rollback()
            else:
                conn.commit()
    else:
        conn.commit()
