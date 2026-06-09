binary = input("Enter binary number: ")

# Add leading zeros to make length a multiple of 3
while len(binary) % 3 != 0:
    binary = "0" + binary

octal = ""

for i in range(0, len(binary), 3):
    group = binary[i:i+3]

    value = 0

    if group[0] == '1':
        value += 4
    if group[1] == '1':
        value += 2
    if group[2] == '1':
        value += 1

    octal += str(value)

print("Octal:", octal)