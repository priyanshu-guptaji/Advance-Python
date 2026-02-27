class College:
    def __init__(self, collegename, **kwargs):
        self.collegename = collegename
        super().__init__(**kwargs)

    def college(self):
        print("College Name:", self.collegename)


class Student(College):
    def __init__(self, name, rollno, section, **kwargs):
        self.name = name
        self.rollno = rollno
        self.section = section
        super().__init__(**kwargs)

    def student(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Section:", self.section)


class Marks(Student):
    def __init__(self, sub1, sub2, sub3, sub4, **kwargs):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        super().__init__(**kwargs)

    def total(self):
        return self.sub1 + self.sub2 + self.sub3 + self.sub4


class SportsMarks(Student):
    def __init__(self, sportsmarks, **kwargs):
        self.sportsmarks = sportsmarks
        super().__init__(**kwargs)


class StudentReport(Marks, SportsMarks):
    def __init__(self, collegename, name, rollno, section,
                 sub1, sub2, sub3, sub4, sportsmarks):

        super().__init__(collegename=collegename,
                         name=name,
                         rollno=rollno,
                         section=section,
                         sub1=sub1,
                         sub2=sub2,
                         sub3=sub3,
                         sub4=sub4,
                         sportsmarks=sportsmarks)

    def report(self):
        academic_total = self.total()
        grand_total = academic_total + self.sportsmarks

        print("\n----- STUDENT REPORT -----")
        self.college()
        self.student()
        print("Academic Total:", academic_total)
        print("Sports Marks:", self.sportsmarks)
        print("Grand Total:", grand_total)


# Object Creation
s1 = StudentReport("GIET University", "Priyanshu", 101, "CSE-A",
                   70, 65, 80, 75, 20)

s1.report()