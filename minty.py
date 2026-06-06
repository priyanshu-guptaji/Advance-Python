def total(n, length):
    total = n

    for i in range(2, length + 1):
        total = 2 * total - 1

    return total

n = int(input())
length = int(input())

print(total(n, length))