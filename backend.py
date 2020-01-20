import sqlite3

class Database:                         
    
    def __init__(self,db):                                 # Making connection--Self must be given otherwise throws error if no argument given
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()                                      #id in above is to get good control of how many entries in databases
        conn.close()

    def insert(self,title,author,year,isbn):               # To addd entries via 'Add entry' button on gui
        conn=sqlite3.connect("book.db")                    # Previsous connect fucntion closes the connection so need to make a new1
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()                                      # Changes made so commit here
        conn.close()

    def view(self):
        conn=sqlite3.connect("book.db")                    # Previsous connect fucntion closes the connection so need to make a new1
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()                                #we need rows to show as tuples data
        conn.close()                                       # No changes made so no commit here 
        return rows                                        #Just data is stored as before. now showing 

    def search(self,title="",author="",year="",isbn=""):   #Set default values as empty strings
        conn=sqlite3.connect("book.db") 
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.close() 
        return rows                                        #Just data is stored as before. now showing 

    def delete(self,id):
        conn=sqlite3.connect("book.db") 
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()                                      # Changes made so commit here
        conn.close()

    def update(self,id,title,author,year,isbn):
        conn=sqlite3.connect("book.db") 
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?",(title,author,year,isbn,id)) # Remember the order.id at last
        conn.commit()                                      # Changes made so commit here
        conn.close()

## Test commands

#connect()
#insert("The time", "Sandra", 1955, 676767384890)
#delete(3)
#update(5,"Just Earth","Dickens",1943,243384890)
#print(view())


#print(search(author="Jackie"))

#::::::Testing output
# connect()
# insert("The book", "Jack", 1924, 353384890)
# print(view()


##::::: Data Samples
#[(1, 'The book', 'Jack', 1924, 353384890), (2, 'The sea', 'Jan', 1934, 353384890), (4, 'The Earth', 'Jackie', 1946, 793384890), 
#(5, 'Just Earth', 'Dickens', 1943, 243384890), (6, 'The sun', 'Sam', 1950, 883384890), (7, 'MyBook', 'Sally', 1965, 8338389339), (8, 'Thegullu', 'gulla', 1970, 3729389238239), 
