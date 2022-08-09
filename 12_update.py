import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Canyon 123", "Yellow Garden 2")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")