import pandas as pd
import sqlite3
import csv

#create a database connection
con = sqlite3.connect("contact.db")
cursor =con.cursor()

# save the csv file in a varibale conatcs 
contacts='contacts.csv'
print(contacts)

#  create a table in a database if not created 
cursor.execute('''
CREATE TABLE IF NOT EXISTS USER_INFO (
	id	INTEGER NOT NULL,
	first_name	TEXT NOT NULL,
	last_name	TEXT NOT NULL,
	email	 TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
)'''
)

#now read the csv file to insert it in a table user_info
with open(contacts,'r') as file:
    reader=csv.DictReader(file)
    for read in reader:
        first_name = read['first_name']
        last_name = read['last_name']
        email = read['email']

# this will insert the entry in a table
        cursor.execute('INSERT INTO USER_INFO (first_name,last_name ,email) VALUES (?, ?,?)', (first_name,last_name, email))

con.commit()
con.close()



