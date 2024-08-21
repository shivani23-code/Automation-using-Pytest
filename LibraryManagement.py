class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self._books):
            raise ValueError("Book with this ISBN already exists")
        self._books.append(book)

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self._books.remove(book)
        else:
            raise ValueError("Book not found")

    def find_book(self, isbn):
        return next((b for b in self._books if b.isbn == isbn), None)

    def list_books(self):
        return self._books
