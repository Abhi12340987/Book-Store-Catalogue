import sqlite3

def connection():
    conn= sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))    
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("app_4_book_store_catalogue/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()




connection()
#insert("Little Red Riding Hood", "Carrie Fish", 1998, 10346)
#delete(7)
update(6, "Effective Habits", "Tom Smooth", 2020, 1107)
print(view())
#print(search(title="The earth"))
