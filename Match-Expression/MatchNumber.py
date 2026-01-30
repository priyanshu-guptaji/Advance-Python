num = int(input("Enter number: "))

match num:
    case 10: 
        print("Ten")
    case 20: 
        print("Twenty")
    case 30:
        print("Thirty")
    case _:
        print("Other number")
