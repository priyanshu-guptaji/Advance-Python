def check(n, m, k):
    if (2 * n * m) % k == 0:
        return "YES"
    return "NO"

n = int(input())
m = int(input())
k = int(input())
print(check(n, m, k))