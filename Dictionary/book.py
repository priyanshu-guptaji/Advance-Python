book = {
    "title": "Life Lessons",
    "author": "Priyanshu Gupta",
    "year": 2026,
    "price": 99,
    "chapters": {
        1: "Introduction",
        2: "Human Behaviour",
        3: "Human Tendency",
        4: "Think with Heart, not Brain",
        5: "Always Brain is not Right"
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