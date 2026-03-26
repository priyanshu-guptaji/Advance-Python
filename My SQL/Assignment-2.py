import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user="root", password="2005")

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS GIETU")
# print("Database created")

cursor.execute("USE GIETU")

# cursor.execute("DROP TABLE IF EXISTS student")

# cursor.execute("""
# CREATE TABLE student(
# id INT PRIMARY KEY,
# name VARCHAR(50),
# age INT
# )
# """)

# print("Table created")

# sql = "INSERT INTO student (id,name,age) VALUES (%s,%s,%s)"



# cursor.executemany(sql, values)

# mydb.commit()



cursor.execute("SELECT * FROM student")
for row in cursor:
    print(row)

cursor.execute("UPDATE student SET marks = 23 WHERE name = 'Priyanshu Gupta'")
mydb.commit()

print("After Update:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM student WHERE name = 'Neha Verma'")
mydb.commit()

print("After Delete:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

cursor.close()
mydb.close()