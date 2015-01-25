import sqlite3 as lite

con = lite.connect('text.db')

cur = con.cursor()

name = 'Andres'
phone = '3366858'
email = 'user@example.com'
password = '12345'

sql = """INSERT INTO users(name, phone, email, password) 
			VALUES('{}', '{}', '{}', '{}')""".format(name, phone, email, password)

try:
	cur.execute(sql)
	# cur.execute("""INSERT INTO users(name, phone, email, password) 
	# 	 VALUES('Welser', '3513251', 'wel@gmail.com', '1234')""")
	# cur.execute("""INSERT INTO users(name, phone, email, password) 
	# 	 VALUES('Orlando', '3554625', 'orlan@gmail.com', '12345')""")
	# cur.execute("""INSERT INTO users(name, phone, email, password) 
	# 	 VALUES('Stuard', '3571056', 'stuard@gmail.com', '123')""")
	# cur.execute("""INSERT INTO users(name, phone, email, password) 
	# 	 VALUES('Yolanda', '3523454', 'yoli@gmail.com', '123456')""")
	# cur.execute("""INSERT INTO users(name, phone, email, password) 
	# 	 VALUES('Emilio', '3341234', 'emilio@gmail.com', '1234567')""")
	con.commit()
	print("Usuario Insertado")
except Exception as e:
	print(e.args)
finally:
	con.close()