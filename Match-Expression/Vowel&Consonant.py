ch = input("Enter a single alphabet: ").lower()

match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel ")
    case _:
            print("Consonant ")
    
