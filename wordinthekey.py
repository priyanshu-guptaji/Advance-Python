import keyword
keywords = keyword.kwlist

word = input("Enter a word: ")

if word in keywords:
    print("Keyword")
else:
    print("Invalid")