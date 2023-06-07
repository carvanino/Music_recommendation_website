import mysql.connector

# Establish a connection to your MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akinola1",
    database="music_app"
)

# Create a cursor to execute SQL statements
cursor = cnx.cursor()

# Create the "songs" table
create_table_query = """
    CREATE TABLE songs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        artist VARCHAR(255),
        title VARCHAR(255),
        genre VARCHAR(255)
    )
"""
cursor.execute(create_table_query)

# Preprocessed data
preprocessed_data = [
    ("Rihanna", "Love on the Brain", "Pop"),
    ("Chris Brown", "Influential", "Pop"),
    ("Shakira", "Waka Waka", "Reggae"),
    ("Adele", "Hello", "Pop Soul"),
    ("Snoop Dogg", "Sexual Eruption", "Hip Hop")
]

# Insert the preprocessed data into the "songs" table
insert_query = "INSERT INTO songs (artist, title, genre) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, preprocessed_data)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
