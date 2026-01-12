import pytest
from book import Book


class TestBook:

    @pytest.mark.parametrize(
        "author,title",
        [
            ("Автор 1", "Книга 1"),
            ("Автор 2", "Книга 2"),
            ("Автор 3", "Книга 3"),
        ]
    )
    def test_book_creation(self, author, title):
        book = Book(author, title)

        assert book.author_name == author
        assert book.title == title
        assert book.id is not None