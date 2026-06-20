"""Core database operations for the Library Management System.

This file keeps the SQLite logic separate from the command-line menu in main.py.
The project is intentionally simple and beginner-friendly for IYU 228.
"""

from __future__ import annotations

import sqlite3
from datetime import date
from pathlib import Path
from typing import Iterable, Optional

DB_FILE = "library.db"


def get_connection(db_path: str = DB_FILE) -> sqlite3.Connection:
    """Create and return a SQLite connection."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_database(db_path: str = DB_FILE) -> None:
    """Create database tables if they do not already exist."""
    schema_path = Path(__file__).with_name("database.sql")
    with get_connection(db_path) as conn:
        conn.executescript(schema_path.read_text(encoding="utf-8"))
        conn.commit()


def add_book(title: str, author: str, isbn: str, publication_year: Optional[int], db_path: str = DB_FILE) -> int:
    """Add a new book and return its ID."""
    with get_connection(db_path) as conn:
        cursor = conn.execute(
            """
            INSERT INTO books (title, author, isbn, publication_year, status)
            VALUES (?, ?, ?, ?, 'Available')
            """,
            (title.strip(), author.strip(), isbn.strip(), publication_year),
        )
        conn.commit()
        return int(cursor.lastrowid)


def list_books(db_path: str = DB_FILE) -> list[sqlite3.Row]:
    """Return all books ordered by ID."""
    with get_connection(db_path) as conn:
        return conn.execute("SELECT * FROM books ORDER BY book_id").fetchall()


def add_member(full_name: str, email: str, phone: str = "", db_path: str = DB_FILE) -> int:
    """Add a new library member and return their ID."""
    with get_connection(db_path) as conn:
        cursor = conn.execute(
            """
            INSERT INTO members (full_name, email, phone)
            VALUES (?, ?, ?)
            """,
            (full_name.strip(), email.strip().lower(), phone.strip()),
        )
        conn.commit()
        return int(cursor.lastrowid)


def list_members(db_path: str = DB_FILE) -> list[sqlite3.Row]:
    """Return all members ordered by ID."""
    with get_connection(db_path) as conn:
        return conn.execute("SELECT * FROM members ORDER BY member_id").fetchall()


def borrow_book(book_id: int, member_id: int, db_path: str = DB_FILE) -> str:
    """Borrow an available book for an existing member."""
    with get_connection(db_path) as conn:
        book = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,)).fetchone()
        member = conn.execute("SELECT * FROM members WHERE member_id = ?", (member_id,)).fetchone()

        if book is None:
            return "Book not found."
        if member is None:
            return "Member not found."
        if book["status"] == "Borrowed":
            return "This book is already borrowed."

        conn.execute(
            """
            INSERT INTO borrowings (book_id, member_id, borrow_date, status)
            VALUES (?, ?, ?, 'Active')
            """,
            (book_id, member_id, date.today().isoformat()),
        )
        conn.execute("UPDATE books SET status = 'Borrowed' WHERE book_id = ?", (book_id,))
        conn.commit()
        return "Book borrowed successfully."


def return_book(book_id: int, db_path: str = DB_FILE) -> str:
    """Return a borrowed book."""
    with get_connection(db_path) as conn:
        active_borrowing = conn.execute(
            """
            SELECT * FROM borrowings
            WHERE book_id = ? AND status = 'Active' AND return_date IS NULL
            """,
            (book_id,),
        ).fetchone()

        if active_borrowing is None:
            return "No active borrowing record found for this book."

        conn.execute(
            """
            UPDATE borrowings
            SET return_date = ?, status = 'Returned'
            WHERE borrowing_id = ?
            """,
            (date.today().isoformat(), active_borrowing["borrowing_id"]),
        )
        conn.execute("UPDATE books SET status = 'Available' WHERE book_id = ?", (book_id,))
        conn.commit()
        return "Book returned successfully."


def list_borrowings(db_path: str = DB_FILE) -> list[sqlite3.Row]:
    """Return borrowing records with book and member names."""
    with get_connection(db_path) as conn:
        return conn.execute(
            """
            SELECT
                br.borrowing_id,
                b.title AS book_title,
                m.full_name AS member_name,
                br.borrow_date,
                br.return_date,
                br.status
            FROM borrowings br
            JOIN books b ON br.book_id = b.book_id
            JOIN members m ON br.member_id = m.member_id
            ORDER BY br.borrowing_id
            """
        ).fetchall()


def seed_sample_data(db_path: str = DB_FILE) -> None:
    """Insert a small amount of sample data if the database is empty."""
    with get_connection(db_path) as conn:
        book_count = conn.execute("SELECT COUNT(*) AS total FROM books").fetchone()["total"]
        member_count = conn.execute("SELECT COUNT(*) AS total FROM members").fetchone()["total"]

    if book_count == 0:
        add_book("1984", "George Orwell", "9780451524935", 1949, db_path)
        add_book("The Little Prince", "Antoine de Saint-Exupery", "9780156012195", 1943, db_path)
        add_book("Sapiens", "Yuval Noah Harari", "9780062316097", 2011, db_path)

    if member_count == 0:
        add_member("Gorkem Sengul", "gorkem@example.com", "555-000-0000", db_path)
        add_member("Ayse Demir", "ayse@example.com", "555-111-1111", db_path)
