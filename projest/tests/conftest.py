import pytest
from book import Book
from library import Library


@pytest.fixture
def book1():
    return Book("Дж. К. Роулинг", "Гарри Поттер")


@pytest.fixture
def book2():
    return Book("Джордж Оруэлл", "1984")


@pytest.fixture
def library():
    return Library("Тестовая библиотека")