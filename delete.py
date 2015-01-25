import sqlite3 as lite

con = lite.connect('text.db')

cur = con.cursor()

sql = "DELETE FROM users WHERE id = '1'"

try:
	cur.execute(sql)
	con.commit()
	print("Delete ok!!!")
except Exception as e:
	print(e.args)
finally:
	con.close()