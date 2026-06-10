a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

for x in range(max(a), min(b) + 1):

    flag = True

    for i in a:
        if x % i != 0:
            flag = False
    
    for i in b:
        if x % i != 0:
            flag = False


    if flag:
        count += 1

print(count)