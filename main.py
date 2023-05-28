import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_app"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM expenditure")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
