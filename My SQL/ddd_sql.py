import mysql.connector as myconn

# connect
mydb = myconn.connect(
    host="localhost",
    user="root",
    password="2005"
)

cursor = mydb.cursor()

# create database
cursor.execute("CREATE DATABASE IF NOT EXISTS new_db")
print("Database created")

# select database
cursor.execute("USE new_db")

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INT PRIMARY KEY,
    name VARCHAR(20),
    age INT
)
""")

print("Table created")

# insert 5 students
sql = "INSERT INTO student (id,name,age) VALUES (%s,%s,%s)"

values = [
    (1,"Priyanshu",21),
    (2,"Rahul",22),
    (3,"Aman",20),
    (4,"Neha",19),
    (5,"Sahil",23)
]

cursor.executemany(sql, values)

mydb.commit()

print(cursor.rowcount, "students inserted")

# show data
cursor.execute("SELECT * FROM student")

for row in cursor:
    print(row)

db_delete = "Delete from student where name = %s"
db_value=("Shyam")
cursor.execute(db_delete , db_value)
mydb.commit()
print(cursor.rowcount , "Record Deleted Successfully")

