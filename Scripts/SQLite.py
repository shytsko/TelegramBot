import sqlite3

conn = sqlite3.connect("mydb.db", check_same_thread=False)
cur = conn.cursor()

def foo():
    cur.execute("select Decision from tasks where id == 1")
    result = cur.fetchone()
    return result[0]