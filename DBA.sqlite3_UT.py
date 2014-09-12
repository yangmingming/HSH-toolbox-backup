##encoding=utf8

from HSH.DBA.hsh_sqlite3 import Database_schema, prt_all
import sqlite3
import datetime

import HSH.DBA.hsh_sqlite3

def UT_Database_schema():
    try:
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()
        c.execute("CREATE TABLE people (id INTEGER PRIMARY KEY NOT NULL, name TEXT, enroll_date DATE);")
        c.execute("CREATE TABLE salary (id INTEGER PRIMARY KEY NOT NULL, hour_rate INTEGER);")
        c.execute("INSERT INTO people (id, name, enroll_date) VALUES (?, ?, ?)", (1, "Jack", datetime.date(2014,8,15) ) )
        c.execute("INSERT INTO salary (id, hour_rate) VALUES (?, ?)", (1, 25) )
        conn.commit()
    except:
        print "Something Wrong, please delete 'records.db' then proceed"

    db_schema = Database_schema("employee.db")
    print db_schema
    print db_schema.people
    print db_schema.salary
    
UT_Database_schema()