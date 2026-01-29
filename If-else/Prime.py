p=int(input("Enter a number to check Prime or not:"))
if p > 1:
    for i in range(2, p):
        if p % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")
