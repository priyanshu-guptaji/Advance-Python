arr = list(map(int, input().split()))

birds = {}

for i in arr:
    birds[i] = birds.get(i, 0) + 1

print(birds)