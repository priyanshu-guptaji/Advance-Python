class Parent:
    def __init__(self):
        print("This is the parent class.")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call parent constructor according to it print parent class message
        print("This is the child class.")

c=Child()