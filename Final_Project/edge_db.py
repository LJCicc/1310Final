import sqlite3 as sql

conn = sql.connect("edge_db.db")

conn.execute("CREATE TABLE drinks (item_id TEXT, name TEXT, type TEXT, price TEXT, amount TEXT)")

conn.close()

print("Table created successfully")