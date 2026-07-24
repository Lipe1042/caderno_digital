import sqlite3

conn = sqlite3.connect("caderno.db")
cursor = conn.cursor()




cursor.execute("CREATE TABLE sintaxes (id INTEGER, termo TEXT)")