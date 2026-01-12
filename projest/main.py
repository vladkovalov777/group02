from book import Book
from library import Library

library = Library("Городская библиотека")

book1 = Book("Дж. К. Роулинг", "Гарри Поттер и философский камень")
book2 = Book("Джордж Оруэлл", "1984")


library.add_book(book1)
library.add_book(book2)

print("Книги в библиотеке:")
library.show_books()

library.remove_book_by_id(book1.id)

print("\nПосле удаления:")
library.show_books()
