code = int(input("Enter status code: "))

match code:
    case 200:
          print("OK")
    case 404:
          print("Not Found")
    case 500:
          print("Server Error")
    case _:
          print("Unknown status")
