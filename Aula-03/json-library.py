import json
from typing import List
from library import Library, Book

LIBRARY = '''{

    "informacao": {

        "nome": "Biblioteca Municipal de Barbacena",

        "telefones": ["32 3333-3333", "32 9 9999-9999"]

    },

    "livros": {

        "romance": [

            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "copias": 10, "emprestados": 5},

            {"titulo": "Quincas Borba", "autor": "Machado de Assis", "copias": 3, "emprestados": 3},

            {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "copias": 3, "emprestados": 0}

        ],

        "tecnologia": [

            {"titulo": "Java: como programar", "autor": "Deitel", "copias": 5, "emprestados": 4},

            {"titulo": "JavaScript: O Guia Definitivo", "autor": "David Flanagan", "copias": 5, "emprestados": 1},

            {"titulo": "C: como programar", "autor": "Deitel", "copias": 1, "emprestados": 1}

        ],

        "autoajuda": [

            {"titulo": "O Segredo", "autor": "Rhonda Byrne", "copias": 2, "emprestados": 0},

            {"titulo": "O Milagre da Manhã", "autor": "Hal Elrod", "copias": 5, "emprestados": 5},

            {"titulo": "Como Fazer Amigos e Influenciar Pessoas", "autor": "Dale Carnegie", "copias": 15, "emprestados": 8}

        ]

    }
}'''


def check_library(library: str) -> None:
    my_library = create_library_from_json(json.loads(library))
    show_results(my_library)


def create_library_from_json(lib_data: any) -> Library:
    return Library(lib_data["informacao"]["nome"], 
                   get_numbers(lib_data["informacao"]["telefones"]), 
                   get_books(lib_data["livros"]))


def get_numbers(numbers) -> List[str]:
    numbers_list = []
    for number in numbers:
        numbers_list.append(number)
    return numbers_list


def get_books(books) -> List[Book]:
    books_list = []
    for category in books:
        for book in books[category]:
            books_list.append(Book(book["titulo"], book["autor"], int(book["copias"]), int(book["emprestados"]), category))
    return books_list


def show_results(my_library: Library) -> None:
    print(f"\n1) Qual o nome da biblioteca? \n\tR: {my_library.name}")
    print(f"\n2) Quantos telefones a biblioteca possui? \n\tR: {len(my_library.numbers)}")
    print(f"\n3) Quantos livros existem na categoria autoajuda? \n\tR: {sum([book.copies_number + book.borrowed_number  for book in my_library.books if book.category == 'autoajuda'])}")
    print(f"\n4) Quantos livros diferentes a biblioteca possui? \n\tR: {sum([1 for book in my_library.books])}")
    print(f"\n5) Quantos livros totais a biblioteca possui? \n\tR: {sum([book.copies_number + book.borrowed_number  for book in my_library.books])}")
    print(f"\n6) Quantos livros da categoria romance estão emprestados? \n\tR: {sum(book.borrowed_number for book in my_library.books if book.category == 'romance')}")
    print(f"\n7) Qual o autor possui mais livros emprestados? \n\tR: {author_with_most_borrowed_books(my_library.books)}")
    print(f"\n8) Qual o nome do livro com mais cópias? \n\tR: {book_with_more_copies(my_library.books)}")
    print(f"\n9) O nome de cada autor e o nome de cada um dos seus livros. \n\tR: {authors_and_books(my_library.books)}")
    print(f"\n10) Qual a categoria possui mais livros? \n\tR: {category_with_more_books(my_library.books)}")
    print(f"\n11) Qual o livro com o maior título? \n\tR: {biggest_title(my_library.books)}")
    print(f"\n12) Qual o autor com o menor nome? \n\tR: {shortest_authors_name(my_library.books)}\n\n")


def author_with_most_borrowed_books(books: List[Book]) -> str:
    authors = dict()
    for book in books:
        if book.author in authors:
            authors[book.author] += book.borrowed_number
        else: 
            authors[book.author] = book.borrowed_number
    authors = sorted(authors.items(), key = lambda x: x[1], reverse=True)
    return " ".join(map(str, [f"\n\t> {name} com {count} livros emprestados." for name, count in authors if count == authors[0][1]]))



def book_with_more_copies(books: List[Book]) -> str:
    popular_book = dict()
    for book in books:
        popular_book[book.title] = book.copies_number

    popular_book = sorted(popular_book.items(), key = lambda x: x[1], reverse=True)
    return " ".join(map(str, [f"\n\t> \'{name}\' com {count} cópias." for name, count in popular_book if count == popular_book[0][1]]))


def authors_and_books(books: List[Book]) -> str:
    verified_authors = dict()

    for book in books:
        if book.author not in verified_authors:
            verified_authors[book.author] = []
        verified_authors[book.author].append(book.title)
    
    result = ""
    for author in verified_authors:
        result += f"\n\t> {author}:"
        for book in verified_authors[author]:
            result += f"\n\t\t- {book}"
        result += "\n"
    return result

def category_with_more_books(books: List[Book]) -> str:
    categorys = dict()
    for book in books:
        if book.category in categorys:
            categorys[book.category] += book.copies_number
        else: 
            categorys[book.category] = book.copies_number
    categorys = sorted(categorys.items(), key = lambda x: x[1], reverse=True)
    return " ".join(map(str, [f"\n\t> Categoria \'{name}\' com {count} livros." for name, count in categorys if count == categorys[0][1]]))


def biggest_title(books: List[Book]) -> str:
    biggest = ""
    for book in books:
        if len(book.title) > len(biggest):
            biggest = book.title
    return biggest


def shortest_authors_name(books: List[Book]) -> str:
    shortest = books[0].author
    for book in books:
        if len(book.author) < len(shortest):
            shortest = book.author
    return shortest


if __name__ == "__main__":
    check_library(LIBRARY)



