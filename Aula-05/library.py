from typing import List

class Book:
    def __init__(self, title: str, authors: List[str], quantity: int, borrowed: int, pages: int):
        self.title = title
        self.authors = authors
        self.quantity = quantity
        self.borrowed = borrowed
        self.pages = pages

class Address:
    def __init__(self, cep: str, number: int, complement: str):
        self.cep = cep
        self.number = number
        self.complement = complement

class Library:
    def __init__(self, address: Address, books: List[Book]):
        self.address = address
        self.books = books
