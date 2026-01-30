lst = [-1, 2, -3, 4]
pos = []
neg = []

for x in lst:
    if x >= 0:
        pos.append(x)
    else:
        neg.append(x)

print("Positive:", pos)
print("Negative:", neg)
