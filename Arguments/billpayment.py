def bill(name, *prices, discount=0):
    total = sum(prices)
    final_amount = total - (total * discount / 100)

    print(f"Customer: {name}")
    print(f"Total before discount: {total}")
    print(f"Discount: {discount}%")
    print(f"Final amount: {final_amount}")


bill("Priyanshu", 100, 200, 300, discount=10)