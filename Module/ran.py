import random
print(dir(random))

print(random.randint(1, 10))

names = ["Priyanshu", "Rahul", "Aman"]
print(random.choice(names))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)