n = 4567
l = len(str(n))

even = 0
odd = 0

for i in range(0, l):
    digit = int(str(n)[i])

    if digit % 2 == 0:
        even = even + digit
    else:
        odd = odd + digit

print(even)
print(odd)