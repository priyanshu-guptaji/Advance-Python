a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

match op:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/': 
        print(a / b if b != 0 else "Division by zero")
    case _: 
        print("Invalid operator")
