# q2_library_system.py

catalog = {}
borrowed_books = []
members = set()


def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed successfully.")
        else:
            print("Book already borrowed.")
    else:
        print("Book not found.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned.")
    else:
        print("Book was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, "->", details)


def main():
    add_book(catalog, 101, "Python Basics", "John", 2020)
    add_book(catalog, 102, "AI Fundamentals", "David", 2022)
    add_book(catalog, 103, "Machine Learning", "Andrew", 2021)
    add_book(catalog, 104, "Data Science", "James", 2023)

    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)

    print("Registered Members:", members)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    return_book(borrowed_books, 101)

    show_available(catalog, borrowed_books)


main()