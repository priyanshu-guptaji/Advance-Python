def monkeyleft(n, m, p, k, j):

    if n <= 0 or m < 0 or p < 0 or k <= 0 or j <= 0:
        return "Invalid Input"

    banana_monkeys = m // k
    peanut_monkeys = p // j

    fed = banana_monkeys + peanut_monkeys

    if (m % k > 0) and (p % j > 0):
        fed += 1

    return n - fed


n = int(input("Total number of monkeys: "))
k = int(input("Bananas eaten by one monkey: "))
j = int(input("Peanuts eaten by one monkey: "))
m = int(input("Total bananas: "))
p = int(input("Total peanuts: "))

result = monkeyleft(n, m, p, k, j)
print("Monkeys left on tree:", result)