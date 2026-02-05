# Crockery Dictionary
crockery = {
    "shop_name": "Sandeep Kitchen",
    "owner": "Priyanshu Gupta",
    "total_items": 5,
    "items": {
        1: "Dinner Plate",
        2: "Soup Bowl",
        3: "Tea Cup",
        4: "Serving Spoon",
        5: "Glass"
    },
    "Location": "China"
}

print("Initial Dictionary:")
print(crockery)

# get()
print("\nUsing get():")
print("Shop Name:", crockery.get("shop_name"))
print("Owner:", crockery.get("owner"))



print("\nUsing keys():")
print(crockery.keys())


print("\nUsing values():")
print(crockery.values())


print("\nUsing items():")
print(crockery.items())


crockery["city"] = "Gunupur"
print("\nAfter adding city:")
print(crockery)


crockery.update({
    "Location": "India",
    "Price": 5999,
    "Open": "Yes"
})
print("\nAfter update():")
print(crockery)


removed_price = crockery.pop("Price")
print("\nAfter pop():")
print("Removed Price:", removed_price)
print(crockery)

# del keyword
del crockery["Open"]
print("\nAfter deleting 'Open':")
print(crockery)

# # clear()
# temp = crockery.copy()   # backup
# temp.clear()
# print("\nAfter clear():")
# print(temp)


print("\nLooping through dictionary:")
for key, value in crockery.items():
    print(key, ":", value)