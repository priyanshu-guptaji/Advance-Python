n = int(input())

if n % 2 == 1:
    print(2 ** ((n - 1) // 2))
else:
    print(3 ** ((n // 2) - 1))