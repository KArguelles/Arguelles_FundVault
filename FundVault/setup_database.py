import sqlite3

def create_database():
    # Connect to the SQLite database (this will create the database file if it doesn't exist)
    connection = sqlite3.connect('fundvault.db')  # SQLite file-based database
    cursor = connection.cursor()

    # Create the users table (if it doesn't exist)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number TEXT NOT NULL UNIQUE,
                        email TEXT NOT NULL,
                        pin TEXT NOT NULL)''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()



# Call the function to create the database and table
create_database()
