def student(name, age=18, *marks):
    print("Name:", name)
    print("Age:", age)
    
    print("Marks:")
    for mark in marks:
        print(mark)
        

student(
    "Priyanshu",
    20,
    85, 90, 88,
)
