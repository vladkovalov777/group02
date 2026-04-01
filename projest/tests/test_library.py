import pytest


class TestLibrary:

    def test_add_book(self, library, book1):
        library.add_book(book1)

        assert len(library.books) == 1
        assert library.books[0] == book1

    def test_remove_book_by_id(self, library, book1):
        library.add_book(book1)

        result = library.remove_book_by_id(book1.id)

        assert result is True
        assert len(library.books) == 0

    @pytest.mark.parametrize(
        "wrong_id",
        [
            "123",
            "wrong-id",
            "",
        ]
    )
    def test_remove_book_wrong_id(self, library, book1, wrong_id):
        library.add_book(book1)

        result = library.remove_book_by_id(wrong_id)

        assert result is False
        assert len(library.books) == 1
