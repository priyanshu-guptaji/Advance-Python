class GrandFather:
    def land(self):
        print("Grandfather owns 10 acres of land.")

class Father(GrandFather):
    def house(self):
        print("Father owns a 3BHK house.")

class Son(Father):
    def car(self):
        print("Son owns a sports car.")


obj = Son()

obj.land()  
obj.house() 
obj.car()    