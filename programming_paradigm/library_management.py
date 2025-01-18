class Book:
    def __init__(self, title, author):
        """
        Initializes a Book instance with title, author, and availability.

        Args:
            title (str): Book title.
            author (str): Book author.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available.

        Returns:
            bool: True if available, False otherwise.
        """
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): Book instance to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title.

        Args:
            title (str): Title of the book to check out.

        Returns:
            bool: True if checkout is successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Returns a book by title.

        Args:
            title (str): Title of the book to return.

        Returns:
            bool: True if return is successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        available_books = [book.title for book in self._books if book.is_available()]
        print("Available Books:")
        for book in available_books:
            print(book)
