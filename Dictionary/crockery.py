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
    "available": True
}


print("Crockery Details:")
print(crockery)

print("Shop Name:")
print(crockery.get("shop_name"))

print("Owner Name:")
print(crockery.get("owner"))


print("\nCrockery Items:")
print(crockery.get("items"))





