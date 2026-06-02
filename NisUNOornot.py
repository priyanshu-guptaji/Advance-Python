number = int(input())

def sumofdigit(n):
    digit_sum = 0

    while n > 0:
        digit = n % 10
        digit_sum += digit
        n //= 10

    if digit_sum < 10:
        return digit_sum

    return sumofdigit(digit_sum)

result = sumofdigit(number)

if result == 1:
    print("UNO Number")
else:
    print("Not a UNO Number")