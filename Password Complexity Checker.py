import re

def evaluate_password_strength(password):
    """
    Evaluates the strength of a password based on various criteria.

    Args:
        password (str): The password to evaluate.

    Returns:
        tuple: A tuple containing the password strength (str) and a list of feedback messages (list).
    """
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one numeric digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%^&*).")

    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    """
    Main function to prompt user input and provide feedback on password strength.
    """
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter a password to check its strength: ")
        strength, feedback = evaluate_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions:")
            for suggestion in feedback:
                print(f"  - {suggestion}")

        if strength == "Strong":
            print("\nYour password is strong! Great job.")
            break
        else:
            print("\nPlease try again with a stronger password.")

if __name__ == "__main__":
    main()
