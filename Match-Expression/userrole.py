role = input("Enter role: ")

match role:
    case "admin":
          print("All permissions")
    case "user":
          print("Limited permissions")
    case "guest":
          print("Read-only access")
    case _:
          print("Unknown role")
