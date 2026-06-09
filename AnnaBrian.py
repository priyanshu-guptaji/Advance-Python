
def refund(n,k):
    sum=0
    for i in n:
        sum = sum +i
    total = sum/2

    ts =0
    for i in n:
        if i != k:
            ts += i
    
    f = ts/2
    return total - f


n = arr = list(map(int, input().split()))
k =int(input())
print(refund(n,k))

