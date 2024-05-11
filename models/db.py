# db.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        """)
        self.conn.commit()

    def add_author(self, name):
        self.cur.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.conn.commit()

    def delete_author(self, author_id):
        self.cur.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        self.conn.commit()

    def find_author_by_ID(self, author_id):
        self.cur.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        return self.cur.fetchone()

    def add_book(self, title, author_id):
        self.cur.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
        self.conn.commit()

    def delete_book(self, book_id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()

    def find_book_by_ID(self, book_id):
        self.cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        return self.cur.fetchone()

    def get_authors(self):
        self.cur.execute("SELECT * FROM authors")
        return self.cur.fetchall()

    def get_books_by_author(self, author_id):
        self.cur.execute("SELECT * FROM books WHERE author_id = ?", (author_id,))
        return self.cur.fetchall()

    def close(self):
        self.conn.close()
