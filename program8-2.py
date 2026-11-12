class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f"The title of {self.author}'s book {self.title}.")
    def read(self):
        print(f"read the book")
book1 = Book("SKY","Taro")
book2 = Book("Mount", "Jiro")
book2.get_info()
book2.read()