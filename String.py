s="*>#"
a=0
b=0
for i in s:
    if i=='*':
        a+=1
    elif i=='#':
        b+=1
print(a-b)