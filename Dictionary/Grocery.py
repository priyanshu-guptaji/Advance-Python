grocery = {
    "Rice": 60,
    "Wheat": 45,
    "Sugar": 40,
    "Milk": 30,
    "Oil": 150
}

print("Grocery Items and Prices:")
total = 0

for key, value in grocery.items():
    print(key, ":", value)
    total += value

print("\nTotal Price =", total)
