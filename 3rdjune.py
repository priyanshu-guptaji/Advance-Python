def count(n):
    count = 0
    for i in range(0,l):
        digit = int(str(n)[i])
   
        if digit != 0:
         n % digit == 0
         count +=1
    return count
n = 1042
l = len(str(n))
print(count(n))


