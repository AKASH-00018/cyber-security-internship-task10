import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit (0-9).")

    if re.search(r'[^a-zA-Z0-9\s]', password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character (e.g., !, @, #, $).")

    if score == 5:
        strength = "Excellent"
    elif score == 4:
        strength = "Very Strong"
    elif score == 3:
        strength = "Good"
    elif score == 2:
        strength = "Fair"
    else:
        strength = "Poor"

    return strength, feedback

if __name__ == '__main__':
    print("--- Password Strength Analyzer ---")
    password_to_check = input("Enter a password to check its strength: ")

    strength_level, feedback_list = check_password_strength(password_to_check)

    print(f"\nPassword Strength: {strength_level}")

    if feedback_list:
        print("\nTo improve your password, please consider the following:")
        for item in feedback_list:
            print(f"  - {item}")
    else:
        print("\nGreat job! Your password is secure and meets all criteria.")
