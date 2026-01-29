import streamlit as st
import random
import string
import os

# File to store credentials
DB_FILE = "user_data.txt"

# ---------------- PASSWORD RULES ---------------- #
def check_password_rules(password):
    return (
        len(password) >= 6 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)
    )

# ---------------- PASSWORD GENERATOR ---------------- #
def generate_password(length=8):
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        pwd = ''.join(random.choice(chars) for _ in range(length))
        if check_password_rules(pwd):
            return pwd

# ---------------- FILE HANDLING ---------------- #
def save_credentials(username, password):
    with open(DB_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def load_credentials():
    users = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                if "," in line:
                    u, p = line.strip().split(",", 1)
                    users[u] = p
    return users

# ---------------- STREAMLIT UI ---------------- #
st.set_page_config(page_title="Password System", page_icon="🔐")
st.title("🔐 Password Creator & Login System")

menu = st.sidebar.selectbox("Select Option", ["Register", "Login"])
all_users = load_credentials()

# -------- SESSION STATE INIT -------- #
if "password" not in st.session_state:
    st.session_state.password = ""

# ---------------- REGISTER ---------------- #
if menu == "Register":
    st.subheader("📝 Create New Account")

    username = st.text_input("Create Username")

    password_choice = st.radio(
        "Choose Password Option",
        ["Create my own password", "Generate random password"]
    )

    # ---- CREATE OWN PASSWORD ---- #
    if password_choice == "Create my own password":
        pwd = st.text_input("Create Password", type="password")
        st.session_state.password = pwd

        if pwd and not check_password_rules(pwd):
            st.warning(
                "Password must have:\n"
                "- Minimum 6 characters\n"
                "- 1 Uppercase letter\n"
                "- 1 Number\n"
                "- 1 Special character"
            )

    # ---- GENERATE PASSWORD ---- #
    else:
        length = st.number_input("Password Length", min_value=6, value=8)
        if st.button("Generate Password"):
            st.session_state.password = generate_password(length)

        if st.session_state.password:
            st.success(f"Generated Password: {st.session_state.password}")

    # ---- CREATE ACCOUNT BUTTON ---- #
    if st.button("Create Account"):
        password = st.session_state.password

        if not username or not password:
            st.error("Username and password cannot be empty")
        elif username in all_users:
            st.error("Username already exists")
        elif "," in username:
            st.error("Username cannot contain commas")
        elif not check_password_rules(password):
            st.error("Password does not meet security rules")
        else:
            save_credentials(username, password)
            st.success("Account created successfully 🎉")
            st.session_state.password = ""

# ---------------- LOGIN ---------------- #
elif menu == "Login":
    st.subheader("🔑 Login")

    login_user = st.text_input("Username")
    login_pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user in all_users and all_users[login_user] == login_pwd:
            st.success(f"Login Successful! Welcome {login_user} 👋")
        else:
            st.error("Invalid username or password ❌")
