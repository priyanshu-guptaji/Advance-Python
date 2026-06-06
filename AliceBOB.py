def chocolates(n, x):
    y = n - x
    box = 0

    while x != y:
        if x > y:
            x = x - y
            box += y
        else:
            y = y - x
            box += x

    return box

n = int(input("Enter the number of chocolates :"))
x = int(input("Enter the number of chocolate in the box :"))
print(chocolates(n, x))