import pytest
from LibraryManagement import Book, Library

@pytest.fixture
def library():
    return Library()

@pytest.fixture
def book():
    return Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")

def test_add_book(library, book):
    library.add_book(book)
    assert library.find_book(book.isbn) == book

def test_add_duplicate_book(library, book):
    library.add_book(book)
    with pytest.raises(ValueError):
        library.add_book(book)

def test_remove_book(library, book):
    library.add_book(book)
    library.remove_book(book.isbn)
    assert library.find_book(book.isbn) is None

def test_remove_nonexistent_book(library):
    with pytest.raises(ValueError):
        library.remove_book("0000000000")

def test_find_book(library, book):
    library.add_book(book)
    found_book = library.find_book(book.isbn)
    assert found_book == book

def test_list_books(library, book):
    library.add_book(book)
    assert len(library.list_books()) == 1
