import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_book(collector):
    collector.add_new_book("Дюна")
    return collector

@pytest.fixture
def collector_with_book_and_genre(collector_with_book):
    collector_with_book.set_book_genre("Дюна", "Фантастика")
    return collector_with_book
