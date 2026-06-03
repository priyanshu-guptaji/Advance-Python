def hcf(n, m):
    while n > 0 and m > 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    return n + m

def lcm(a, b):
    return (a * b) // hcf(a, b)

n=int(input("Enter first Number:"))
m=int(input("Enter Second Number:"))
print("HCF: ",hcf(n,m))
print("LCM: ",lcm(n,m))