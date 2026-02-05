dict = {"name" : "ram" , "roll no" : 101 , "marks" : {0 , 70 ,80} , "College" : "GIET"}
print(dict)


x = dict.get("marks")
print(x)

x = dict.values()
print(x)

x = dict.keys()
print(x)

if "college" in dict:
    print("College is present then go to college and complete 80% criteria .")
else:
    print("No Valid Keyword")

dict['College'] = "GIETU"
print(dict)

dict.update({"Attendance" : "Present"})
print(dict)