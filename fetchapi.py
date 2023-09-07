import requests
import sqlite3
api = 'https://openlibrary.org/books/OL7353617M.json'
# send get request 
r = requests.get(api)

#if request success full
if r.status_code == 200:
    print("Success in sending request")
else:
    print("Failed to fetch data from the API.")

# parsed the json data
b_data=r.json()

con=sqlite3.connect('contact.db')
cur=con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS BOOK_DATA
 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT , 
author TEXT,
publish_year  DATE
)''')

#insert data in our database

title = b_data.get('title', '')
author = ', '.join([author['key'] for author in b_data.get('authors', [])])
publish_year = b_data.get('publish_date', '')

cur.execute('INSERT INTO BOOK_DATA (title, author, publish_year) VALUES (?, ?, ?)',
                   (title, author, publish_year))
    
con.commit()

print ("Data inserted successfully into table ")

# retrieve the data 

cur.execute('SELECT * FROM BOOK_DATA')
book=cur.fetchall()

for b in book:
    print("Book ID:", b[0])
    print("Title:", b[1])
    print("Author:", b[2])
    print("Publish Date:", b[3])
    print("\n")

con.close()


