class Library:
    def __init__(self):
        self.books = []
    def display_books(self):
        if self.books:
            for i, box in enumerate(self.books):
                print(f"{i+1}.{box}")
        else:
            print("There is no book.")
    def borrow_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"borrowed {book_title}")
        else:
            print(f"There is no {book_title}.")
    def return_book(self, book_title):
        self.books.append(book_title)

lib = Library()
#lib.display_books()
lib.borrow_book("book4")
#lib.return_book("book5")
lib.display_books()