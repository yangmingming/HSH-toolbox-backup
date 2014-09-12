##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

import psycopg2

def insertmany(conn, c, cmd, records):
    '''INSERT INTO tablename VALUES (%s, %s, ...)
    '''
    try:
        c.executemany(cmd, records)
    except psycopg2.IntegrityError:
        conn.rollback() # rollback 然后试着逐条insert
        for record in records:
            try:
                c.execute(cmd, record)
            except psycopg2.IntegrityError:
                conn.rollback()
            else:
                conn.commit()
    else:
        conn.commit()
