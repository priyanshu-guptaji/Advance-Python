class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def greet(self):
        print(f"Hello, I am {self.name}")
        print(f"I am {self.age} years old")
        print(f"My branch is {self.branch}")


s1 = Student("Priyanshu Gupta", 20, "CSE")
s1.greet()