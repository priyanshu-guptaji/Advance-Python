n = int(input("Enter a number to check whether it is Happy Number or not: "))

def happy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)

        total = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            total += digit * digit
            temp //= 10

        n = total

    return n

result = happy(n)

if result == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")