def stu(**info):
    print("name of student",info["name"])
    print("blood group of student",info["blood_group"])
    print(len(info))
    print(type(info))

stu(name="Priyanshu Gupta",
    age=21,blood_group="B+",
    city="Ranchi")