import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should have at least one special character (e.g., !, @, #).")
    if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
        strength = "Strong"
    elif sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]) >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
