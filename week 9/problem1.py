from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

book1 = Book('Catcher in the Rye', 'Jerome David Salinger', 288)
book2 = Book('Catcher in the Rye', 'Jerome David Salinger', 288)

print(book1)
print(book1 == book2)