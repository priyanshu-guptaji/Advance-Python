arr = [1, 2, 3, 4, 3, 2, 1]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break