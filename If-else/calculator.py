def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ch = int(input("Enter choice: "))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if ch == 1:
    print("Result:", add(x, y))
elif ch == 2:
    print("Result:", sub(x, y))
elif ch == 3:
    print("Result:", mul(x, y))
elif ch == 4:
    print("Result:", div(x, y))
else:
    print("Invalid choice")
