class Person:
    def info(self):
        print("I am Person and My name is Doraemon")

class Teacher(Person):
    def tech(self):
        print("I mark absent to students.")

class SubjectTeacher(Teacher):
    def subject(self):
        print("A for Apple")


obj = SubjectTeacher()

obj.info()      
obj.tech()      
obj.subject()  