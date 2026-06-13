text = input().upper()
key = int(input())

result = ""

for ch in text:
    if ch.isalpha():
        pos = ord(ch) - ord('A')
        pos = (pos + key) % 26
        result += chr(pos + ord('A'))
    else:
        result += ch

print(result)