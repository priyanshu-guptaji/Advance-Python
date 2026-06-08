arr = list(map(int, input().split()))

birds = {}

for i in arr:
    birds[i] = birds.get(i, 0) + 1

max_count = 0
ans = 0

for i in birds:
    if birds[i] > max_count:
        max_count = birds[i]
        ans = i
    elif birds[i] == max_count and i < ans:
        ans = i

print(ans)