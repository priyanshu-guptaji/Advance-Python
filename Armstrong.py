def arm(n):
    original = n
    power = len(str(n))
    total = 0

    while n > 0: 
        digit = n % 10
        total += digit ** power
        n //= 10

    return total == original


n = int(input("Enter a number: "))

if arm(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")