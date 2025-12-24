import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength rating
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium 🙂"
    else:
        strength = "Weak ⚠️"

    return strength, feedback


# Example usage
password = input("Enter a password: ")
strength, tips = check_password_strength(password)

print("\nPassword Strength:", strength)
if tips:
    print("Suggestions:")
    for tip in tips:
        print("-", tip)
