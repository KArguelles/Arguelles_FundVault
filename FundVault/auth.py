# auth.py
# This file contains the logic for user signup and login.

# In-memory list to store user data (for simulation, no actual database).
users = []

# Function to handle signup
def signup(first_name, last_name, phone_number, email, pin):
    # Check if the phone number already exists
    if any(user['phone_number'] == phone_number for user in users):
        return False, "Phone number is already registered."

    # Create a new user
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'email': email,
        'pin': pin
    }

    # Add the new user to the users list
    users.append(new_user)
    return True, "Signup successful!"

# Function to handle login
def login(phone_number, pin):
    # Check if the user exists and the PIN matches
    user = next((user for user in users if user['phone_number'] == phone_number), None)
    if user and user['pin'] == pin:
        return True, "Login successful!"
    return False, "Invalid phone number or PIN."

