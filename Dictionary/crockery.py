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
    "Location":"China" 
}


print("\nCrockery Details:")
print(crockery)

print("\nShop Name:")
print(crockery.get("shop_name"))

print("\nOwner Name:")
print(crockery.get("owner"))


print("\nCrockery Items:")
print(crockery.get("items"))

crockery['Location'] = "India"
print(crockery)

crockery.update({"Attendance" : "Present"})
print(crockery)

crockery["city"] = "Gunupur"
print(crockery)

crockery.update({"Section" : "CSE-I"})
print(crockery)





