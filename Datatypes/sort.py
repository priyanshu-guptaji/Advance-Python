lst = [4, 1, 3, 2]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Ascending:", lst)


print("Descending:", lst[::-1])
