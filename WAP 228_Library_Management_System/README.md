# WAP 228 - Library Management System

This project was prepared for the **IYU 228 Workplace Practice** course. It is a beginner-friendly command-line library management system developed with **Python**, **SQLite**, and **GitHub**.

## Project Purpose

The aim of this project is to create a simple system that helps a small library manage books, members, and borrowing records. The application allows the user to add books, add members, borrow books, return books, and list records.

## Technologies Used

- Python 3
- SQLite
- GitHub
- Standard Python libraries only

No external package installation is required.

## Features

- Add a new book
- List all books
- Add a new member
- List all members
- Borrow a book
- Return a book
- List borrowing records
- Insert sample data for testing

## Database Structure

The project uses three main tables:

### books

Stores book information.

| Column           | Description           |
| ---------------- | --------------------- |
| book_id          | Unique book ID        |
| title            | Book title            |
| author           | Book author           |
| isbn             | Unique ISBN number    |
| publication_year | Publication year      |
| status           | Available or Borrowed |

### members

Stores library member information.

| Column    | Description          |
| --------- | -------------------- |
| member_id | Unique member ID     |
| full_name | Member name          |
| email     | Unique email address |
| phone     | Phone number         |

### borrowings

Stores borrowing and return operations.

| Column       | Description         |
| ------------ | ------------------- |
| borrowing_id | Unique borrowing ID |
| book_id      | Related book ID     |
| member_id    | Related member ID   |
| borrow_date  | Date of borrowing   |
| return_date  | Date of return      |
| status       | Active or Returned  |

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python main.py
```

On Windows, if `python` does not work, try:

```bash
py main.py
```

## Example Usage

After running the program, the menu will be displayed:

```text
===== Library Management System =====
1. Add Book
2. List Books
3. Add Member
4. List Members
5. Borrow Book
6. Return Book
7. List Borrowing Records
8. Insert Sample Data
0. Exit
```

First, you can choose option `8` to insert sample data. Then you can list books and members, borrow a book, and return it.

## Test Cases

The project includes simple unit tests inside the `tests` folder. To run the tests:

```bash
python -m unittest discover tests
```

## Author

Görkem Şengül  
Computer Engineering  
OSTİM Technical University
