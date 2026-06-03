def digits(n, m):
    count = 0

    for i in range(n, m + 1):
        digit = str(i)

        if digit[0] != digit[1]:
            count += 1

    return count

print(digits(11, 15))