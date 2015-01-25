import sqlite3 as lite

con = lite.connect('text.db')
print("Database Conexion abierta")

cur = con.cursor()

sql = """ CREATE TABLE users (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					phone TEXT NOT NULL,
					email TEXT UNIQUE NOT NULL,
					password TEXT NOT NULL)"""
try:
	cur.execute(sql)
	con.commit()
	print("Tabla users creada")
except Exception as e:
	print(e.args)
finally:
	con.close()