arr = list(map(int, input().split()))

result = []

for x in arr:
    if x != 0:
        result.append(x)

while len(result) < len(arr):
    result.append(0)

print(result)