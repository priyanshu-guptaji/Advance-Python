def count_unique(n1,n2):
    count = 0
    for i in range(n1 , n2+1):
        s = str(i)
        if len(s) == len(set(s)):
            count +=1
    return count
n1 = int(input())
n2 = int(input())

result = count_unique(n1,n2)
print(result)