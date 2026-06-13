d = {'A': 1,'B': 2,'D': 1,'O': 1,'P': 1,'Q': 1,'R': 1}
n = input("Enter a string: ").capitalize()
c = 0
for i in n:
    if i in d:
        c += d[i]

print(c)