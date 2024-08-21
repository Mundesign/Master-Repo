import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Query to list columns of the 'store_product' table
cursor.execute("PRAGMA table_info(store_product);")

# Fetch and print column details
columns = cursor.fetchall()
for column in columns:
    print(column)

# Close the connection
conn.close()
