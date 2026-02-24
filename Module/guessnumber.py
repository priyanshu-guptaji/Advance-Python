import random

number = random.randint(1, 100)   
limit = 3                       

print("Guess the number between 1 and 50")
print("You have", limit, "attempts")

for i in range(limit):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed in", i+1, "attempts")
        break
    elif guess > number:
        print("Too High!")
    else:
        print("Too Low!")

else:
    print("Game Over")
    print("The number was:", number)