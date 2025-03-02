# =============================================================
# LIBRARY MANAGEMENT SYSTEM
# =============================================================

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"Book '{book.title}' has been borrowed.")
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Book '{book.title}' has been returned.")
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{book} - {status}")


# Example usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "1234567891")

    library.add_book(book1)
    library.add_book(book2)

    while True:
        print("\nLibrary Menu:")
        print("1. Display books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            isbn = input("Enter the ISBN of the book to borrow: ")
            library.borrow_book(isbn)
        elif choice == "3":
            isbn = input("Enter the ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")