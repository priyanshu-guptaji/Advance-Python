def decimal_to_octal(n):
    if n == 0:
        return "0"
    
    octal = ""

    while n > 0:
        octal = str(num % 8) + octal
        num //= 8

    return octal

num = int(input("Enter a Deciaml Number"))
print("Octal Number = " , decimal_to_octal(num))