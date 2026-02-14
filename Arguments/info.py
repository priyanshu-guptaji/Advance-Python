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
