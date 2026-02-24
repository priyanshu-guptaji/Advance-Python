def bank(customer, bank_name, account_number, balance=10000):
    print(f"{customer} has an account in {bank_name} with account number {account_number}.")
    print(f"Current Balance: ₹{balance}")

bank("Priyanshu Gupta", "State Bank Of India", 1234567890)


def bank_d(name, balance, bank="SBI"):
    print("Name:", name)
    print("Bank:", bank)
    print("Initial Balance:", balance)

    balance += 2000
    print("Deposited:", 2000)

    balance += 1500
    print("Deposited:", 1500)

    balance -= 1000
    print("Withdrawn:", 1000)

    balance -= 500
    print("Withdrawn:", 500)

    print("Final Balance:", balance)
    print()

bank_d("Rahul", 10000)
bank_d("Anita", 15000, "HDFC")