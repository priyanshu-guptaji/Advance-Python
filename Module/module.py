import calculator
print(calculator.add(10, 5))
print(calculator.sub(52,7))
print(calculator.mul(52 ,78))
print(calculator.div(49,7))

print(dir(calculator))



for name in dir(calculator):
    if not name.startswith("__"):
        print(name)