"""
nmn
"""

import sqlite3
con = sqlite3.connect("music.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Writers")
cur.execute("CREATE TABLE Writers(Id INTEGER PRIMARY KEY, Name VARCHAR(25))")

# con.close()

cur.execute("INSERT INTO Writers (Id, Name) VALUES (?, ?)", (1, "Jack London"))
cur.execute("INSERT INTO Writers (Id, Name) VALUES (?, ?)", (2, "Honore de Balzac"))
cur.execute("INSERT INTO Writers (Id, Name) VALUES (?, ?)", (3, "Lion Feuchtwanger"))
cur.execute("INSERT INTO Writers (Id, Name) VALUES (?, ?)", (4, "Emile Zola"))
cur.execute("INSERT INTO Writers (Id, Name) VALUES (?, ?)", (5, "Truman Capote"))

con.commit()

print("Writers: ")
cur.execute("SELECT * FROM Writers WHERE Id <= 4")

#Fetch the Records
rows  = cur.fetchall()

for row in rows:
    print(f"{row[0]}. {row[1]}")
    # print(row)

#Update Name on whose Id = 4

print("")
#Prompt User to insert name that will be updated into the Table
name = input("Enter the name (first and last) to be updated (e.g: 'John Doe'): ")
cur.execute("UPDATE Writers SET Name = ? WHERE Id = 4", (name,))

con.commit()

#Close Connection
cur.close()

