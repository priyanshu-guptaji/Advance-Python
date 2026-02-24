def bill(name, *prices, discount=0):
    total = sum(prices)
    finalamount = total - (total * discount / 100)

    print(f"Customer: {name}")
    print(f"Total before discount: {total}")
    print(f"Discount: {discount}%")
    print(f"Final amount: {finalamount}")


bill("Priyanshu Gupta", 100, 200, 300, discount=10)