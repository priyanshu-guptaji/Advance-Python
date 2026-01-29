
x=int(input("Enter first Number:"))
y=int(input("Enter second Number:"))
z=int(input("Enter third Number:"))
if(x > y and x > z):
    print(x," is greater then ",y, " and " ,z)
elif(y > x and y > z ):
    print(y," is greater then ",x, " and " ,z)
elif(z > x and z > y ):
    print(z," is greater then ",x, " and " ,y)
else:
    print("Not Defined")
