def armstrong(num):
    n = len(str(num))

    total = 0
    temp = num
    while num > 0:
        digit = num % 10
        total = total + digit ** n
        temp //= 10

    return total == num

num = int(input("Enter a Number:"))
if armstrong(num):
    print("Armstrong Number")

else :
    print("Not an Armstrong Number")


