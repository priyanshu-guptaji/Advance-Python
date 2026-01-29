ch = input("Enter choice (1-7) to know the day: ")

match ch:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday (Weekend)")
    case "7":
        print("Sunday (Weekend)")
    case _:
        print("Invalid choice")
