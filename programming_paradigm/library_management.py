class Book:
    def __init__(self, title, author):
        self.title = title               
        self.author = author              
        self._is_checked_out = False      

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have checked out '{book.title}'.")
                return
        print(f"'{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    print(f"'{title}' was not checked out.")
                else:
                    book.return_book()
                    print(f"You have returned '{book.title}'.")
                return
        print(f"'{title}' does not exist in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")   