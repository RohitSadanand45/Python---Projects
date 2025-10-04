import random
import string
import os

# File to store username & passwords
DB_FILE = "user_data.txt"

# Function to check password rules
def check_password_rules(password):
    return (
        len(password) >= 6 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)
    )

# Function to generate random Password
def generate_password(length=8):
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if check_password_rules(password):
            return password

# Function to save credentials
def save_credentials(username, password):
    with open(DB_FILE, "a") as f:
        f.write(f"{username},{password}\n")

# Function to load credentials
def load_credentials():
    creds = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                if "," in line:
                    user, pwd = line.strip().split(",", 1)
                    creds[user] = pwd
    return creds

# === Main Program ===
print("=== Password Creator & Login ===")

# Load existing users
all_users = load_credentials()

# Ask for username (and check duplicate)
while True:
    username = input("Create Username: ").strip()
    if username in all_users:
        print("Username already exists! Please choose another.")
    elif ',' in username:
        print(" Username cannot contain commas.")
    else:
        break

# Choose password option
print("\nDo you want to:")
print("1. Create your own password")
print("2. Generate a random password")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    while True:
        password = input("Create Password: ").strip()
        if check_password_rules(password):
            print("Password accepted.")
            break
        else:
            print("Password must have:")
            print("- Minimum 6 characters")
            print("- At least 1 uppercase letter")
            print("- At least 1 number")
            print("- At least 1 special character")
elif choice == "2":
    length_input = input("Enter desired password length (minimum 6): ")
    try:
        length = int(length_input)
    except ValueError:
        length = 8
    password = generate_password(length)
    print(" Your generated password is:", password)
else:
    print("Invalid choice. Defaulting to generated password of length 8.")
    password = generate_password()

# Save new credentials
save_credentials(username, password)
print(" Account created successfully!")

#  Reload all users (to include the newly saved one)
all_users = load_credentials()

# Simulate login
print("\n=== Login ===")
login_user = input("Enter Username: ").strip()
login_pwd = input("Enter Password: ").strip()

if login_user in all_users and all_users[login_user] == login_pwd:
    print(f" Login Successful! Welcome, {login_user}")
else:
    print(" Invalid username or password.")
