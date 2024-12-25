from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Initialize SparkSession
spark = SparkSession.builder.appName("InsecurePasswordExample").getOrCreate()

# Hardcoded passwords - BAD PRACTICE
users_data = [
    ("admin", "123456"),  # Weak password
    ("user1", "password"),
    ("user2", "qwerty"),
]

# Hardcoded account keys - BAD PRACTICE
keys_data = [
    ("admin", "ADMIN_KEY_12345"),
    ("user1", "USER1_KEY_ABCDE"),
    ("user2", "USER2_KEY_XYZ"),
]

users_df = spark.createDataFrame(users_data, ["username", "password"])
keys_df = spark.createDataFrame(keys_data, ["username", "account_key"])


# Insecure user authentication - BAD PRACTICE
def authenticate(username, password):
    user = users_df.filter(
        (users_df.username == username) & (users_df.password == password)
    ).collect()
    if user:
        print(f"Welcome {username}!")
        return True
    else:
        print("Authentication failed.")
        return False


# Logging sensitive data to console - BAD PRACTICE
def log_sensitive_data():
    print("Logging all sensitive data...")
    users_df.show()
    keys_df.show()


# Generating a new account key - BAD PRACTICE
def generate_account_key(username):
    import random

    key = f"{username}_{random.randint(1000, 9999)}"  # Weak random generation
    global keys_df
    new_key = spark.createDataFrame([(username, key)], ["username", "account_key"])
    keys_df = keys_df.union(new_key)
    print(f"Generated key for {username}: {key}")
    return key


# Register a new user - BAD PRACTICE
def register_user(username, password):
    if users_df.filter(users_df.username == username).count() > 0:
        print("User already exists!")
    else:
        global users_df
        new_user = spark.createDataFrame(
            [(username, password)], ["username", "password"]
        )
        users_df = users_df.union(new_user)
        print(f"User {username} registered with password: {password}")


# Hardcoded API key - BAD PRACTICE
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
        if users_df.filter(users_df.username == username).count() > 0:
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
