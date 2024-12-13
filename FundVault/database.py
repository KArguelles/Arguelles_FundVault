import mysql.connector
from mysql.connector import Error

def create_connection():
    print("Connecting to database...")
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='fvault_db',
            user='root', 
            password='' 
        )
        print("Connection successful")
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def register_user(first_name, last_name, phone_number, email, pin):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO users (first_name, last_name, phone_number, email, pin) VALUES (%s, %s, %s, %s, %s)"
            values = (first_name, last_name, phone_number, email, pin)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "User registered successfully"
        except Error as e:
            cursor.close()
            connection.close()
            return False, f"Error: {e}"

    return False, "Failed to connect to the database"

# Function to check login credentials
def check_login(phone_number, pin):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = "SELECT * FROM users WHERE phone_number = %s AND pin = %s"
            cursor.execute(query, (phone_number, pin))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                return True, result  # Return the user data
            return False, "Invalid credentials"
        except Error as e:
            cursor.close()
            connection.close()
            return False, f"Error: {e}"

    return False, "Failed to connect to the database"

