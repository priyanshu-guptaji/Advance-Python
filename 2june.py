# for i in range(50,101,22):
#     print(i)
sum = 0
for i in range(1,100):
    sum = sum +i
print(sum)




number = 123
digit_sum = 0
while number > 0:

    digit = number % 10
    digit_sum += digit
    number //= 10
print("The sum of digits is:", digit_sum)

