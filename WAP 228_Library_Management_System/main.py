"""Command-line interface for the Library Management System."""

from __future__ import annotations

import sqlite3
from typing import Optional

from library_service import (
    add_book,
    add_member,
    borrow_book,
    initialize_database,
    list_books,
    list_borrowings,
    list_members,
    return_book,
    seed_sample_data,
)


def read_int(prompt: str) -> Optional[int]:
    """Read an integer from the user. Return None if invalid."""
    value = input(prompt).strip()
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        print("Please enter a valid number.")
        return None


def print_books() -> None:
    books = list_books()
    print("\n--- Books ---")
    if not books:
        print("No books found.")
        return

    for book in books:
        print(
            f"ID: {book['book_id']} | Title: {book['title']} | Author: {book['author']} | "
            f"ISBN: {book['isbn']} | Year: {book['publication_year']} | Status: {book['status']}"
        )


def print_members() -> None:
    members = list_members()
    print("\n--- Members ---")
    if not members:
        print("No members found.")
        return

    for member in members:
        print(
            f"ID: {member['member_id']} | Name: {member['full_name']} | "
            f"Email: {member['email']} | Phone: {member['phone']}"
        )


def print_borrowings() -> None:
    records = list_borrowings()
    print("\n--- Borrowing Records ---")
    if not records:
        print("No borrowing records found.")
        return

    for record in records:
        return_date = record["return_date"] if record["return_date"] else "Not returned yet"
        print(
            f"ID: {record['borrowing_id']} | Book: {record['book_title']} | "
            f"Member: {record['member_name']} | Borrowed: {record['borrow_date']} | "
            f"Returned: {return_date} | Status: {record['status']}"
        )


def handle_add_book() -> None:
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    publication_year = read_int("Publication year: ")

    if not title or not author or not isbn:
        print("Title, author, and ISBN are required.")
        return

    try:
        book_id = add_book(title, author, isbn, publication_year)
        print(f"Book added successfully. New book ID: {book_id}")
    except sqlite3.IntegrityError:
        print("A book with this ISBN already exists.")


def handle_add_member() -> None:
    full_name = input("Full name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    if not full_name or not email:
        print("Full name and email are required.")
        return

    try:
        member_id = add_member(full_name, email, phone)
        print(f"Member added successfully. New member ID: {member_id}")
    except sqlite3.IntegrityError:
        print("A member with this email already exists.")


def handle_borrow_book() -> None:
    book_id = read_int("Book ID: ")
    member_id = read_int("Member ID: ")
    if book_id is None or member_id is None:
        return
    print(borrow_book(book_id, member_id))


def handle_return_book() -> None:
    book_id = read_int("Book ID: ")
    if book_id is None:
        return
    print(return_book(book_id))


def show_menu() -> None:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Member")
    print("4. List Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. List Borrowing Records")
    print("8. Insert Sample Data")
    print("0. Exit")


def main() -> None:
    initialize_database()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add_book()
        elif choice == "2":
            print_books()
        elif choice == "3":
            handle_add_member()
        elif choice == "4":
            print_members()
        elif choice == "5":
            handle_borrow_book()
        elif choice == "6":
            handle_return_book()
        elif choice == "7":
            print_borrowings()
        elif choice == "8":
            seed_sample_data()
            print("Sample data inserted if the database was empty.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
