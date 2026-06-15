inp = input("Enter numbers: ").split()

n = len(inp)

for i in range(n - 1):
    for j in range(n - 1 - i):

        if len(inp[j]) > len(inp[j + 1]):

            inp[j], inp[j + 1] = inp[j + 1], inp[j]

        elif len(inp[j]) == len(inp[j + 1]) and int(inp[j]) > int(inp[j + 1]):

            inp[j], inp[j + 1] = inp[j + 1], inp[j]

print(inp)