import mysql.connector as myconn

mydb = myconn.connect(host="localhost" , user = "root" , password = "2005")

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS GIETU")
print("Database created")

cursor.execute("USE GIETU")

# cursor.execute("""
# CREATE TABLE student(
# id INT PRIMARY KEY,
# name VARCHAR(50),
# age INT
# )
# """)

# print("Table created")

# sql = "INSERT INTO student (id,name,age) VALUES (%s,%s,%s)"

# values = [
#     (1,"Priyanshu",21),
#     (2,"Rahul",22),
#     (3,"Aman",20),
#     (4,"Neha",19),
#     (5,"Sahil",23)
# ]

# cursor.executemany(sql, values)

# mydb.commit()

# print(cursor.rowcount, "students inserted")


cursor.execute("SELECT * FROM student")
for row in cursor:
    print(row)



