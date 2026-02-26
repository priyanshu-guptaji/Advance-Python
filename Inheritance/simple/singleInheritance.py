class Car:  
    def __init__(self, brand):
        self.brand = brand
    def run(self):
        return f"{self.brand} car is running"
class Child(Car):   
    def prop(self):
        return "This is a child class method"
c = Child("BMW")
print(c.run())   
print(c.prop()) 