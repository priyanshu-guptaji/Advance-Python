def emp_d(name, department="General", **details):
    print("Name:", name)
    print("Department:", department)
    for k, v in details.items():
        print(k + ":", v)
    print()

emp_d("Raunak", age=25, salary=40000, city="Hyderabad")

emp_d("Anita", "IT", age=28, salary=60000, experience="3 years")

emp_d("Karan", "HR", age=30, salary=50000, city="Bhubaneswar")