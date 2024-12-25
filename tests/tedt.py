import os
import random

# Hardcoded passwords - BAD PRACTICE
users = {"admin": "123456", "user1": "password", "user2": "qwerty"}  # Weak password

# Account keys stored in plaintext - BAD PRACTICE
account_keys = {
    "admin": "ADMIN_KEY_12345",
    "user1": "USER1_KEY_ABCDE",
    "user2": "USER2_KEY_XYZ",
}


# Function to authenticate user
# This uses insecure password verification - BAD PRACTICE
def authenticate(username, password):
    if username in users and users[username] == password:
        print(f"Welcome {username}!")
        return True
    else:
        print("Authentication failed.")
        return False


# Logging sensitive data to console - BAD PRACTICE
def log_sensitive_data():
    print("Logging all sensitive data...")
    print("Users:", users)
    print("Account Keys:", account_keys)


# Generating a new account key - BAD PRACTICE
# No entropy and insecure randomness
def generate_account_key(username):
    key = f"{username}_{random.randint(1000, 9999)}"
    account_keys[username] = key
    print(f"Generated key for {username}: {key}")
    return key


# Function to register a new user - BAD PRACTICE
# No input sanitization or validation
def register_user(username, password):
    if username in users:
        print("User already exists!")
    else:
        users[username] = password
        print(f"User {username} registered with password: {password}")


# Hardcoding API keys in the script - BAD PRACTICE
API_KEY = "MY_SECRET_API_KEY"

# Handling user input insecurely - BAD PRACTICE
while True:
    print("1. Register User")
    print("2. Authenticate User")
    print("3. Generate Account Key")
    print("4. Log Sensitive Data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authenticate(username, password)
    elif choice == "3":
        username = input("Enter username: ")
        if username in users:
            generate_account_key(username)
        else:
            print("User not found.")
    elif choice == "4":
        log_sensitive_data()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
