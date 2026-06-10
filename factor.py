a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

for x in range(max(a), min(b) + 1):

    valid = True

    for i in a:
        if x % i != 0:
            valid = False
            break

    if valid:
        for j in b:
            if j % x != 0:
                valid = False
                break

    if valid:
        count += 1

print(count)