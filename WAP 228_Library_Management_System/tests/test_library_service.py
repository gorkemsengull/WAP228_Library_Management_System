import tempfile
import unittest
from pathlib import Path

from library_service import (
    add_book,
    add_member,
    borrow_book,
    initialize_database,
    list_books,
    list_borrowings,
    list_members,
    return_book,
)


class LibraryServiceTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_library.db")
        initialize_database(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_book(self):
        book_id = add_book("1984", "George Orwell", "9780451524935", 1949, self.db_path)
        books = list_books(self.db_path)
        self.assertEqual(book_id, 1)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "1984")

    def test_add_member(self):
        member_id = add_member("Gorkem Sengul", "gorkem@example.com", "555", self.db_path)
        members = list_members(self.db_path)
        self.assertEqual(member_id, 1)
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0]["email"], "gorkem@example.com")

    def test_borrow_and_return_book(self):
        book_id = add_book("Sapiens", "Yuval Noah Harari", "9780062316097", 2011, self.db_path)
        member_id = add_member("Ayse Demir", "ayse@example.com", "555", self.db_path)

        borrow_result = borrow_book(book_id, member_id, self.db_path)
        self.assertEqual(borrow_result, "Book borrowed successfully.")
        self.assertEqual(list_books(self.db_path)[0]["status"], "Borrowed")

        return_result = return_book(book_id, self.db_path)
        self.assertEqual(return_result, "Book returned successfully.")
        self.assertEqual(list_books(self.db_path)[0]["status"], "Available")

        borrowings = list_borrowings(self.db_path)
        self.assertEqual(len(borrowings), 1)
        self.assertEqual(borrowings[0]["status"], "Returned")


if __name__ == "__main__":
    unittest.main()
