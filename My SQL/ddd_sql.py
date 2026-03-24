import mysql.connector as myconn
mydb = myconn.connect(host="localhost" , user="root" , password="2005")
print("Connection created")