# Creating a dictionary
student = {
    "name": "Ram",
    "roll_no": 101,
    "age": 20,
    "marks": [70, 80, 90],
    "passed": True
}


print("Dictionary:", student) #Dictionary: {'name': 'Ram', 'roll_no': 101, 'age': 20, 'marks': [70, 80, 90], 'passed': True}


print("Name:", student["name"])  #Name: Ram
print("Marks:", student.get("marks"))
print("Keys:", student.keys()) 
print("Values:", student.values())
print("Items:", student.items())
student["city"] = "Delhi"
print("After adding city:", student)
