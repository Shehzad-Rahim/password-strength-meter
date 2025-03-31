import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("Password Checker & Generator")


pw = st.text_input("Enter your password", type="password")

feedback = []
score = 0

# List of blacklisted passwords
blacklist = ["password123", "123456", "qwerty", "letmein", "welcome", "admin", "passw0rd"]

if pw:
    if pw in blacklist:
        feedback.append("❌ This is a common password and is too weak. Please choose a different one.")
    else:
        # Custom scoring weights
        length_weight = 2
        case_weight = 1.5
        number_weight = 1.5
        special_weight = 2

        if len(pw) >= 8:
            score += length_weight
        else:
            feedback.append("❌ Password must be at least 8 characters long.")

        if re.search(r'[a-z]', pw) and re.search(r'[A-Z]', pw):
            score += case_weight
        else:
            feedback.append("❌ Password must contain at least one uppercase and lowercase letter.")

        if re.search(r'[0-9]', pw):
            score += number_weight
        else:
            feedback.append("❌ Password must contain at least one number.")

        if re.search(r'[%@!#*&$]', pw):
            score += special_weight
        else:
            feedback.append("❌ Password must contain at least one special character(%@!#*&$).")

        # Password strength evaluation
        if score >= 6:
            feedback.append("✅ Your Password is Strong")
        elif score >= 4:
            feedback.append("🟨 Your Password is Moderate, could be stronger")
            st.warning("Your password might be vulnerable to brute force attacks.")
            st.info("Consider adding a unique, random sequence of characters to enhance security.")
        else:
            feedback.append("🔶 Your Password is Weak, consider adding more characters and special characters.")
            st.info("Your password might be vulnerable to brute force attacks.")
            st.warning("Consider adding a unique, random sequence of characters to enhance security.")

    if feedback:
        st.markdown("## Suggestions")
        for fd in feedback:
            st.write(fd)
else:
    st.info("Enter any password to check the strength")


# Password Generator Function
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "%@!#*&$"
    return ''.join(random.choice(characters) for _ in range(length))

# Add a password generator button
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"Generated Password: `{strong_password}`")
