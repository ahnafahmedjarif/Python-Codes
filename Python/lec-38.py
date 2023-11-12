# Exercise - 6

class Library:

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addBook(self , book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        print(f"The new added book is {book}")

    def showInfo(self):
        print(f"This library has {self.no_of_books} books")
        for item in self.books:
            print(f"The all books are {item}")

l1 = Library()
# l1.addBook("Harry Potter")
l1.addBook("XYZ Harry Potter")
l1.showInfo()