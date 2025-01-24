from oop import book_class
def main():
    book = book_class.Book("1984", "George Orwell", 1949)
    print(book)
    print(repr(book))
    del book
if __name__ == "__main__":
    main()