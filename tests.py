import pytest


class TestBooksCollector:

    def test_add_new_book_len_more_then_40_false(self, collector):
        name = 'Что делать, если ваш кот хочет вас убить и съесть'
        collector.add_new_book(name)

        assert collector.books_genre.get(name) is None

    def test_add_new_book_without_genre_true(self, collector):
        name = 'Идиот'
        collector.add_new_book(name)

        assert collector.books_genre[name] == ''

    def test_set_book_genre(self, collector):
        name = '12 стульев'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre.get(name) == genre

    def test_set_book_genre_books_genre_not_in_genre(self, collector):
        name = '12 стульев'
        genre = 'Мелодрама'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert genre not in collector.genre and collector.books_genre.get(name) != genre

    def test_get_book_genre(self, collector):
        name = '12 стульев'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        book_genre = collector.get_book_genre(name)

        assert book_genre == genre

    def test_get_books_with_specific_genre(self, collector):
        amount_of_fantastic = 2

        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        specific_genre = collector.get_books_with_specific_genre('Фантастика')

        assert len(specific_genre) == amount_of_fantastic

    def test_get_books_genre(self, collector):
        name = '12 стульев'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        books_genre = collector.get_books_genre()

        assert name in books_genre and books_genre[name] == genre

    def test_get_books_for_children_genre_in_genre_age_rating(self, collector):
        children_book = 'Карлсон'
        children_genre = 'Мультфильмы'
        collector.add_new_book(children_book)
        collector.set_book_genre(children_book, children_genre)

        not_children_book = 'Оно'
        not_children_genre = 'Ужасы'
        collector.add_new_book(not_children_book)
        collector.set_book_genre(not_children_book, not_children_genre)

        books_for_children = collector.get_books_for_children()

        assert children_book in books_for_children and not_children_book not in books_for_children

    def test_add_book_in_favorites(self, collector):
        book = '12 стульев'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        favorite = collector.get_list_of_favorites_books()

        assert book in favorite

    @pytest.mark.parametrize(
        'name,books_count',
        [
            (['12 стульев'], 1),
            (['Гарри Поттер', 'Идиот'], 2),
            ([], 0)
        ]
    )
    def test_add_book_in_favorites_add_a_few_books(self, collector, name, books_count):
        for book_name in name:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        favorite = collector.get_list_of_favorites_books()

        assert len(favorite) == books_count

    def test_delete_book_from_favorites(self, collector):
        book = '12 стульев'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        favorite = collector.get_list_of_favorites_books()

        assert len(favorite) == 0

    def test_get_list_of_favorites_books(self, collector):
        first_book = '12 стульев'
        second_book = 'Идиот'
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.add_book_in_favorites(first_book)

        favorite = collector.get_list_of_favorites_books()

        assert first_book in favorite and len(favorite) == 1