import pytest

import data

from main import BooksCollector

class TestBooksCollector:
    @pytest.mark.parametrize('book_name', ['Десять негритят', 'Тот, кто живёт в колодце', 'Антидемон',
                                           'Бравый солдат Швейк', 'Манюня', '12 стульев', 'Дядя Стёпа'])
    def test_books_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_name_long_name_book_more_40_characters_not_add(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить!')
        assert len(collector.get_books_genre()) == 0

    def test_add_name_zero_name_book_not_add(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_only_one_book(self, collector):
        collector.add_new_book(data.TestData.new_book_name)
        collector.add_new_book(data.TestData.new_book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_books_genre(self, collector):
        collector.add_new_book(data.TestData.new_book_name)
        collector.set_book_genre(data.TestData.new_book_name, data.TestData.new_book_genre)
        assert collector.get_books_genre() == {'Десять негритят':'Детективы'}

    def test_set_books_genre_no_genre_list(self, collector):
        collector.add_new_book(data.TestData.new7_book_name)
        collector.set_book_genre(data.TestData.new7_book_genre, data.TestData.new7_book_genre)
        assert collector.get_books_genre() == {'Дядя Стёпа': ''}

    def test_get_book_genre(self, collector):
        collector.add_new_book(data.TestData.new_book_name)
        collector.set_book_genre(data.TestData.new_book_name, data.TestData.new_book_genre)
        assert collector.get_book_genre(data.TestData.new_book_name) == 'Детективы'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book(data.TestData.new4_book_name)
        collector.set_book_genre(data.TestData.new4_book_name, data.TestData.new4_book_genre)
        collector.add_new_book(data.TestData.new2_book_name)
        collector.set_book_genre(data.TestData.new2_book_name, data.TestData.new2_book_genre)
        collector.add_new_book(data.TestData.new6_book_name)
        collector.set_book_genre(data.TestData.new6_book_name, data.TestData.new6_book_genre)
        assert collector.get_books_with_specific_genre('Комедии') == ['Бравый солдат Швейк', '12 стульев']

    def test_get_book_for_children(self, collector):
        collector.add_new_book(data.TestData.new5_book_name)
        collector.set_book_genre(data.TestData.new5_book_name, data.TestData.new5_book_genre)
        collector.add_new_book(data.TestData.new3_book_name)
        collector.set_book_genre(data.TestData.new3_book_name, data.TestData.new3_book_genre)
        assert collector.get_books_with_specific_genre(data.TestData.new5_book_genre) == ['Манюня']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book(data.TestData.new3_book_name)
        collector.add_book_in_favorites(data.TestData.new3_book_name)
        assert collector.get_list_of_favorites_books() == ['Антидемон']

    def test_add_book_in_favorites_only_one_book(self, collector):
        collector.add_new_book(data.TestData.new3_book_name)
        collector.add_book_in_favorites(data.TestData.new3_book_name)
        collector.add_book_in_favorites(data.TestData.new3_book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_remove_book_from_favorites(self, collector):
        collector.add_new_book(data.TestData.new3_book_name)
        collector.add_book_in_favorites(data.TestData.new3_book_name)
        collector.delete_book_from_favorites(data.TestData.new3_book_name)
        assert collector.get_list_of_favorites_books() == []

    def test_get_favorites_books(self, collector):
        collector.add_new_book(data.TestData.new6_book_name)
        collector.add_book_in_favorites(data.TestData.new6_book_name)
        assert collector.get_list_of_favorites_books() == ['12 стульев']

    def test_add_favorites_book_add_two_books(self, collector):
        collector.add_new_book(data.TestData.new3_book_name)
        collector.add_new_book(data.TestData.new6_book_name)
        collector.add_book_in_favorites(data.TestData.new3_book_name)
        collector.add_book_in_favorites(data.TestData.new6_book_name)
        assert collector.get_list_of_favorites_books() == ['Антидемон', '12 стульев']

    def test_remove_favorites_book_only_one_book(self, collector):
        collector.add_new_book(data.TestData.new_book_name)
        collector.add_book_in_favorites(data.TestData.new_book_name)
        collector.add_new_book(data.TestData.new2_book_name)
        collector.add_book_in_favorites(data.TestData.new2_book_name)
        collector.delete_book_from_favorites(data.TestData.new2_book_name)
        assert collector.get_list_of_favorites_books() == ['Десять негритят']
