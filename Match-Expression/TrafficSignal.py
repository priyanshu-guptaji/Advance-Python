s = input("Enter signal: ")

match s:
    case "R":
        print("Red 🔴 Stop")
    case "Y":
        print("Yellow 🟡 Ready")
    case "G":
        print("Green 🟢 Go")
    case "O":
        print("Orange 🟠 Slow")
    case _:
        print("Invalid signal ❌")