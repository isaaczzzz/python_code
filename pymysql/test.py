import pymysql

conn = pymysql.connect(host="117.50.187.219", user="root", password="123456")

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version: %s." % data)

cursor.close()
conn.close()