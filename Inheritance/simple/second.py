class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def display(self):
        print("This is the child class.")

c=Child()
c.display()
c.show()