# WAP 228 Workplace Practice Project Report

## Project Title

Library Management System

## Student Information

Name: Görkem Şengül  
Department: Computer Engineering  
University: OSTİM Technical University  
Course: WAP 228 Workplace Practice

## 1. Introduction

This project is a simple Library Management System developed for the IYU 228 Workplace Practice course. The main purpose of the project is to manage books, members, and borrowing records in a small library environment. The system was developed using Python and SQLite.

## 2. Project Purpose

The purpose of this project is to create a basic software application that can store library data and perform common library operations. These operations include adding books, listing books, adding members, borrowing books, returning books, and viewing borrowing records.

## 3. Technologies Used

The project was developed with the following technologies:

- Python 3
- SQLite database
- GitHub for version control and project sharing
- Command-line interface

Python was selected because it is easy to read and suitable for beginner-level software development. SQLite was selected because it is lightweight and does not require a separate database server.

## 4. Database Design

The database includes three main tables: books, members, and borrowings.

### 4.1 Books Table

The books table stores book information such as title, author, ISBN, publication year, and status. The status field shows whether the book is available or borrowed.

### 4.2 Members Table

The members table stores library member information. Each member has a unique email address.

### 4.3 Borrowings Table

The borrowings table stores the relationship between books and members. It records the borrow date, return date, and borrowing status.

## 5. System Features

The application includes the following features:

1. Add a new book
2. List all books
3. Add a new member
4. List all members
5. Borrow a book
6. Return a book
7. List borrowing records
8. Insert sample data

## 6. Implementation

The project is divided into two main Python files. The `main.py` file includes the command-line menu and user input operations. The `library_service.py` file includes database operations such as adding books, adding members, borrowing books, and returning books.

The database structure is stored in the `database.sql` file. When the program starts, the database tables are created automatically if they do not exist.

## 7. Testing

Simple unit tests were added in the `tests` folder. These tests check important functions such as adding books, adding members, borrowing a book, and returning a book.

The tests can be run with this command:

```bash
python -m unittest discover tests
```

## 8. Result

As a result, a working library management system was developed. The project uses Python and SQLite to perform basic database operations. The system is simple, understandable, and suitable for the requirements of the IYU 228 Workplace Practice course.

## 9. GitHub Repository

The project will be uploaded to a public GitHub repository. The repository will include source code, database script, README file, and project documentation.
