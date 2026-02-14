def student(info):
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Blood Group:", info["blood group"])
    print("City:", info["city"])

info = {
    "name": "Priyanshu Gupta",
    "age": 20,
    "blood group": "B+",
    "city": "Delhi"
}

student(info)

students = [
    {
        "name": "Priyanshu Gupta",
        "age": 20,
        "blood group": "B+",
        "city": "Delhi"
    },
    {
        "name": "Vinayak Tripathy",
        "age": 21,
        "blood group": "O+",
        "city": "Mumbai"
    }
]

# Using for loop
for info in students:
    student(info)
