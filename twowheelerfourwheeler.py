def vehicle(v, w):
    if w >= 2 and (w % 2 == 0) and v < w:
        y = (w - 2 * v) // 2   
        x = v - y              
        return x, y
    else:
        return "INVALID INPUT"

v = int(input("Enter number of vehicles: "))
w = int(input("Enter number of wheels: "))

print(vehicle(v, w))