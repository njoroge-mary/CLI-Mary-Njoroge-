# main.py
from models.db import Database
from models.models import Author, Book

def main():
    db = Database("books.db")
    db.create_tables()

    while True:
        print("\n1. Add Author")
        print("2. Add Book")
        print("3. View Authors")
        print("4. View Books by Author")
        print("5. Delete Author")
        print("6. Find Author by ID")
        print("7. Delete Book")
        print("8. Find Book by ID")
        print("9. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter author name: ")
            db.add_author(name)
            print("Author added successfully!")

        elif choice == "2":
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            db.add_book(title, author_id)
            print("Book added successfully!")

        elif choice == "3":
            authors = db.get_authors()
            print("\nAuthors:")
            for author in authors:
                print(f"{author[0]}. {author[1]}")

        elif choice == "4":
            author_id = int(input("Enter author ID: "))
            books = db.get_books_by_author(author_id)
            print("\nBooks by Author:")
            for book in books:
                print(f"{book[0]}. {book[1]}")

        elif choice == "5":
            author_id = int(input("Enter author ID to delete: "))
            db.delete_author(author_id)
            print("Author deleted successfully!")

        elif choice == "6":
            author_id = int(input("Enter author ID to find: "))
            author = db.find_author_by_ID(author_id)
            if author:
                print(f"Author found: {author[1]}")
            else:
                print("Author not found.")

        elif choice == "7":
            book_id = int(input("Enter book ID to delete: "))
            db.delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == "8":
            book_id = int(input("Enter book ID to find: "))
            book = db.find_book_by_ID(book_id)
            if book:
                print(f"Book found: {book[1]}")
            else:
                print("Book not found.")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    db.close()

if __name__ == "__main__":
    main()
