import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

# Create table
cur.execute(
    """CREATE TABLE movies
               (name text)"""
)

# Insert a row of data
cur.execute("INSERT INTO movies VALUES ('First Movie')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
