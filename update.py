import sqlite3 as lite

con = lite.connect('text.db')

cur = con.cursor()

sql = "UPDATE users SET name = 'WelserJr' WHERE id='2'"

try:
	cur.execute(sql)
	con.commit()
	print("Update Succesfull!!!")
except Exception as e:
	print(e.args)
finally:
	con.close()