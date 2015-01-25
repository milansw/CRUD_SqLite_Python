import sqlite3 as lite

con = lite.connect('text.db')

cur = con.cursor()

sql = """SELECT id, name, phone, email, password
		 FROM users"""

try:
	# cur.execute(sql)
	#Trae 1 sola fila de la tabla
	# user1 = cur.fetchone()
	# print("ID: ", user1[0])
	# print("NAME: ", user1[1])
	# print("PHONE: ", user1[2])
	# print("EMAIL: ", user1[3])
	# print("PASSWORD: ", user1[4])

	# Trae fila segun id ingresado
	userid = int(input("Ingrese id: "))
	cur.execute("""SELECT id, name, phone, email, password
		 		   FROM users 
		           WHERE id='{}'""".format(userid))
	user = cur.fetchone()
	print("ID: ", user[0])
	print("NAME: ", user[1])
	print("PHONE: ", user[2])
	print("EMAIL: ", user[3])
	print("PASSWORD: ", user[4])

	#Trae todas las filas de la tabla
	# results = cur.fetchall()
	# for row in results:
	# 	print("ID: ", row[0])
	# 	print("NAME: ", row[1])
	# 	print("PHONE: ", row[2])
	# 	print("EMAIL: ", row[3])
	# 	print("PASSWORD: ", row[4], "\n")
		#print(row)
except Exception as e:
	print(e.args)
finally:
	con.close()