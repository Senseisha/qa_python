import pytest

from .main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        # collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


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

        assert collector.books_genre.get(name) != genre

    def test_get_book_genre(self, collector):
        name = '12 стульев'
        collector.add_new_book(name)
        book_genre = collector.get_book_genre(name)

        assert book_genre == collector.books_genre.get(name)

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
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')

        dict = collector.get_books_genre()

        assert '12 стульев' in dict

    def test_get_books_for_children(self, collector):
        book = 'Карлсон'
        collector.add_new_book(book)
        collector.set_book_genre(book, 'Мультфильмы')

        books_for_children = collector.get_books_for_children()

        assert book in books_for_children

    def test_get_books_for_children_genre_in_genre_age_rating(self, collector):
        book = 'Оно'
        collector.add_new_book(book)
        collector.set_book_genre(book, 'Ужасы')

        books_for_children = collector.get_books_for_children()

        assert book not in books_for_children

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
        book = '12 стульев'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        favorite = collector.get_list_of_favorites_books()

        assert len(favorite) > 0