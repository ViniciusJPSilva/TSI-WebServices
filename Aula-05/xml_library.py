from lxml import etree
from library import *

BOOKS = "livros"
ADDR = "endereco"
CEP = "cep"
NUMBER = "numero"
COMPL = "complemento"
QTT = "quantidade"
BORROWED = "emprestados"
TITLE = "titulo"
PAGES = "paginas"
AUTHOR = "autor"
DEITEL = "Deitel"

def main(library_xml_file: str) -> None:
    my_library = create_library_from_xml(etree.parse(library_xml_file))
    show_results(my_library)


def create_library_from_xml(xml: any) -> Library:
    root = xml.getroot()

    addr = root.find(ADDR)
    books = root.find(BOOKS)

    return Library(
                    address = Address(addr.attrib[CEP], int(addr.find(NUMBER).text), addr.find(COMPL).text),
                    books = [
                            Book(title=book.find(TITLE).text, 
                                authors= [author.text for author in book.getchildren() if author.tag == AUTHOR], 
                                quantity = int(book.attrib[QTT]), 
                                borrowed = int(book.attrib[BORROWED]), 
                                pages = int(book.find(PAGES).text)) 
                            for book in books.getchildren()
                        ]
                )

def borrowed_percentage(library: Library) -> float:
    return sum([book.borrowed for book in library.books]) / sum([book.quantity for book in library.books])

def book_with_fewer_pages(library: Library) -> str:
    books = sorted([(book.title, book.pages) for book in library.books], key=lambda tup: tup[1])
    return books[0][0]

def book_with_more_authors(library: Library) -> str:
    more_authors = dict()
    for book in library.books:
        more_authors[book.title] = len(book.authors)

    more_authors = sorted(more_authors.items(), key = lambda x: x[1], reverse=True)
    return " ".join(map(str, [f"\n\t> \'{title}\' com {count} autores." for title, count in more_authors if count > 1]))

def show_results(library: Library) -> None:
    print(f"\n1) Qual a porcentagem de livros da biblioteca que estão emprestados? \n\tR: {borrowed_percentage(library) * 100: .2f} %")
    print(f"\n2) Quantos títulos diferentes do autor \"Deitel\" a biblioteca possui? \n\tR: {sum([1 for book in library.books for author in book.authors if author == DEITEL])}")
    print(f"\n3) Qual o nome do livro da biblioteca que possui menos páginas? \n\tR: {book_with_fewer_pages(library)}")
    print(f"\n4) Qual o nome do livro (ou livros) que possui mais de um autor? \n\tR: {book_with_more_authors(library)}")
    

if __name__ == "__main__":
    main('library.xml')
