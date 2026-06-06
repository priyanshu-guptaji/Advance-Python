def digits(n, m):
    count = 0

    for i in range(n, m + 1):
        digit = str(i)

        if len(set(digit)) == len(digit):
            count += 1

    return count

print(digits(11, 150))