import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_init_init_set(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_one_book_len_4_book_added(self, collector):
        collector.add_new_book("Дюна")
        assert "Дюна" in collector.books_genre

    def test_set_book_genre_added_book_fantastic_genre_set(self, collector_with_book):
        collector_with_book.set_book_genre("Дюна", "Фантастика")
        assert collector_with_book.books_genre["Дюна"] == "Фантастика"

    def test_get_book_genre_added_book_fantastic_genre_got(self, collector_with_book_and_genre):
        genre = collector_with_book_and_genre.get_book_genre("Дюна")
        assert genre == "Фантастика"

    def test_get_books_with_specific_genre_added_book_fantastic_book_got(self, collector_with_book_and_genre):
        books = collector_with_book_and_genre.get_books_with_specific_genre("Фантастика")
        assert books == ["Дюна"]

    def test_get_books_genre_added_book_without_genre(self, collector_with_book):
        genres = collector_with_book.get_books_genre()
        assert genres == {"Дюна": ""}

    @pytest.mark.parametrize(
        "books_data, expected_result",
        [
            (
                    [("Незнайка", "Мультфильмы"), ("Плот", "Ужасы")],
                    ["Незнайка"]
            ),
            (
                    [("Горе от ума", "Комедии"), ("Дюна", "Фантастика")],
                    ["Горе от ума", "Дюна"]
            )
        ]
    )
    def test_get_books_for_children(self, collector, books_data, expected_result):
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        result = collector.get_books_for_children()
        assert result == expected_result

    def test_add_book_in_favorites_added_book(self, collector_with_book):
        collector_with_book.add_book_in_favorites("Дюна")
        assert "Дюна" in collector_with_book.favorites

    def test_delete_book_from_favorites(self, collector_with_book):
        collector_with_book.add_book_in_favorites("Дюна")
        collector_with_book.delete_book_from_favorites("Дюна")
        assert "Дюна" not in collector_with_book.favorites

    def test_get_list_of_favorites_books(self, collector_with_book):
        collector_with_book.add_book_in_favorites("Дюна")
        favorites = collector_with_book.get_list_of_favorites_books()
        assert favorites == ["Дюна"]
