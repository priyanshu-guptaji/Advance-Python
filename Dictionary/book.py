
book = {
    "title": "Python Programming",
    "author": "Guido van Rossum",
    "year": 2024,
    "price": 499,
    "chapters": {
        1: "Introduction",
        2: "Variables & Data Types",
        3: "Control Statements",
        4: "Functions",
        5: "Dictionary & Sets"
    },
    "available": True
}


print("Book Details:")
print(book)


print("\nBook Title:", book.get("title"))


print("\nBook Keys:")
print(book.keys())


print("\nBook Values:")
print(book.values())


print("\nBook Items:")
print(book.items())


print("\nChapters:")
print(book.get("chapters"))



