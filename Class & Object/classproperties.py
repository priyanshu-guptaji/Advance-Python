# Access delete modify and Add properties of class and object
class demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"Hello {self.name}, welcome to OOPs in Python!")

d=demo("Priyanshu Gupta", 21)
d.greet()

# Accessing properties
print(d.name)

# Modifying properties
d.name="Sonu"
d.greet()

# Deleting properties
del d.age
#print(d.age) # This will raise an error as age property is deleted

# Adding new properties
d.branch="CSE"
print(d.branch)