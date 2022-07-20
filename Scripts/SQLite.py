import sqlite3
from unittest import result

conn = sqlite3.connect("mydb.db", check_same_thread=False)
cur = conn.cursor()

def SelectOne(req: str):
    cur.execute(req)
    result = cur.fetchone()
    if result == None:
        return ""
    return result[0]

def SelectMore(req: str):
    cur.execute(req)
    result = cur.fetchall()
    return result