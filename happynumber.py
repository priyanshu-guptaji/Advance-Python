n = int(input())

while n != 1 and n != 4:
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit * digit
        temp //= 10

    n = total

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")