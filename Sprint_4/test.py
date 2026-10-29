import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.books_genre = {}
    collector.favorites = []
    return collector


def test_add_new_book(collector):
    collector.add_new_book('Гарри Поттер')

    assert collector.books_genre == {'Гарри Поттер': ''}

@pytest.mark.parametrize('name, expected', [
    ('А', True),
    ('А' * 40, True),
    ('А' * 41, False),
    ('', False),
])

def test_add_new_book_name_length(collector, name, expected):
    collector.add_new_book(name)

    assert (name in collector.books_genre) == expected


def test_add_new_book_duplicate(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')

    assert len(collector.books_genre) == 1


def test_set_book_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert collector.books_genre['Гарри Поттер'] == 'Фантастика'


def test_set_book_genre_invalid(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Романтика')
    assert collector.books_genre['Гарри Поттер'] == ''


def test_set_book_genre_unknown_book(collector):
    collector.set_book_genre('Неизвестная книга', 'Фантастика')
    assert collector.books_genre == {}


def test_get_book_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    result = collector.get_book_genre('Гарри Поттер')
    assert result == 'Фантастика'


def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Оно')
    collector.add_new_book('Марсианин')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Марсианин', 'Фантастика')
    result = collector.get_books_with_specific_genre('Фантастика')
    assert result == ['Гарри Поттер', 'Марсианин']


def test_get_books_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Оно')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    result = collector.get_books_genre()
    assert result == {
        'Гарри Поттер': 'Фантастика',
        'Оно': ''
    }


def test_get_books_for_children(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Оно')
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    result = collector.get_books_for_children()
    assert result == ['Гарри Поттер']


def test_add_book_in_favorites(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert collector.favorites == ['Гарри Поттер']


def test_delete_book_from_favorites(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.delete_book_from_favorites('Гарри Поттер')
    assert collector.favorites == []


def test_get_list_of_favorites_books(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Марсианин')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Марсианин')
    result = collector.get_list_of_favorites_books()
    assert result == ['Гарри Поттер', 'Марсианин']