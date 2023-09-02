from typing import List

class Book:
    def __init__(self, title: str, author: str, copies_number: int, borrowed_number: int, category: str):
        self.title = title
        self.author = author
        self.copies_number = copies_number
        self.borrowed_number = borrowed_number
        self.category = category

class Library :
    def __init__(self, name: str, numbers: List[str], books: List[Book]):
        self.name = name
        self.numbers = numbers
        self.books = books





    