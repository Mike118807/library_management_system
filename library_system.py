from book import Book
from user import User
from author import Author

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter publication date: ")
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        title = input("Enter book title to borrow: ")
        for book in self.books:
            if book.get_title() == title and book.borrow():
                print(f"Book '{title}' borrowed successfully.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.get_title() == title and book.return_book():
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' was not borrowed.")

    def search_book(self):
        title = input("Enter book title to search: ")
        for book in self.books:
            if book.get_title() == title:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Published: {book.get_publication_date()}, Borrowed: {'Yes' if book.is_borrowed() else 'No'}")
                return
        print(f"Book '{title}' not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Published: {book.get_publication_date()}, Borrowed: {'Yes' if book.is_borrowed() else 'No'}")

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter library ID: ")
        for user in self.users:
            if user.get_library_id() == library_id:
                print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")
                return
        print(f"User with ID '{library_id}' not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter author name to view details: ")
        for author in self.authors:
            if author.get_name() == name:
                print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
                return
        print(f"Author '{name}' not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")

    def run(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    print("\nBook Operations:")
                    print("1. Add a new book")
                    print("2. Borrow a book")
                    print("3. Return a book")
                    print("4. Search for a book")
                    print("5. Display all books")
                    print("6. Back to Main Menu")
                    book_choice = input("Enter your choice: ")

                    if book_choice == '1':
                        self.add_book()
                    elif book_choice == '2':
                        self.borrow_book()
                    elif book_choice == '3':
                        self.return_book()
                    elif book_choice == '4':
                        self.search_book()
                    elif book_choice == '5':
                        self.display_all_books()
                    elif book_choice == '6':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            
            elif choice == '2':
                while True:
                    print("\nUser Operations:")
                    print("1. Add a new user")
                    print("2. View user details")
                    print("3. Display all users")
                    print("4. Back to Main Menu")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        self.add_user()
                    elif user_choice == '2':
                        self.view_user_details()
                    elif user_choice == '3':
                        self.display_all_users()
                    elif user_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == '3':
                while True:
                    print("\nAuthor Operations:")
                    print("1. Add a new author")
                    print("2. View author details")
                    print("3. Display all authors")
                    print("4. Back to Main Menu")
                    author_choice = input("Enter your choice: ")

                    if author_choice == '1':
                        self.add_author()
                    elif author_choice == '2':
                        self.view_author_details()
                    elif author_choice == '3':
                        self.display_all_authors()
                    elif author_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == '4':
                print("Quitting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
