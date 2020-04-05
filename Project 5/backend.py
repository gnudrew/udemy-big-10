import sqlite3 as sql

def connect():
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sql.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
   

connect()
# insert("The Sun","John Smith",1918,9819681651)
# delete(2)
update(4,"The Moon", "John Smooth", 1917, 999999)
print(view())
print(search(author="John Smith"))