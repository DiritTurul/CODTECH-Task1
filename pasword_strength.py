import re
import pyfiglet

def password_strength(password):
    print("Calculating password strength...")
    strength = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for digits
    if re.search(r"\d", password):
        strength += 2  # give more weight to digits
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for symbols
    if re.search(r"\W", password):
        strength += 2  # give more weight to symbols
    else:
        feedback.append("Password should contain at least one symbol.")

    # Check against common passwords from file
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
    if password.lower() in common_passwords:
        feedback.append("Password is a common password and should be avoided.")
        strength -= 2  # penalize for using a common password

    # Calculate password strength score
    strength_score = strength
    if strength_score < 2:
        return "Weak", feedback
    elif strength_score < 4:
        return "Moderate", feedback
    else:
        feedback.append("Well done! Your password is strong.")
        return "Strong", feedback
        
    

def main():
    ascii_banner = pyfiglet.figlet_format("Password Strencth Checker")
    print(ascii_banner)
    password = input("Enter a password: ")
    strength, feedback = password_strength(password)
    print("Password strength:", strength)
    print("Feedback:")
    for item in feedback:
        print(item)

if __name__ == "__main__":
    main()