from book import Book

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book_by_id(self, book_id: str):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def show_books(self):
        for book in self.books:
            print(book)
