# Task 3: Password Complexity Checker

import string

def check_password_strength(password):
    """
    Assesses the strength of a password based on several criteria.

    Args:
        password (str): The password string to check.

    Returns:
        tuple: A tuple containing (score, feedback_messages_list).
    """
    score = 0
    feedback = []

    # 1. Length Check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short (should be at least 8 characters).")
    elif length >= 8 and length <= 11:
        score += 1
        feedback.append("Length: Good (8-11 characters).")
    elif length >= 12 and length <= 15:
        score += 2
        feedback.append("Length: Better (12-15 characters).")
    else: # length >= 16
        score += 3
        feedback.append("Length: Excellent (16+ characters).")

    # 2. Character Type Checks
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    # Using string.punctuation for standard special characters
    has_special = any(c in string.punctuation for c in password)

    if has_uppercase:
        score += 1
        feedback.append("Includes uppercase letters.")
    else:
        feedback.append("Missing uppercase letters.")

    if has_lowercase:
        score += 1
        feedback.append("Includes lowercase letters.")
    else:
        feedback.append("Missing lowercase letters.")

    if has_digit:
        score += 1
        feedback.append("Includes numbers.")
    else:
        feedback.append("Missing numbers.")

    if has_special:
        score += 1
        feedback.append("Includes special characters.")
    else:
        feedback.append("Missing special characters.")

    # 3. Overall Strength Rating based on score
    strength_rating = ""
    if score <= 1:
        strength_rating = "Very Weak"
    elif score <= 3:
        strength_rating = "Weak"
    elif score <= 5:
        strength_rating = "Moderate"
    elif score <= 7:
        strength_rating = "Strong"
    else:
        strength_rating = "Very Strong"

    feedback.insert(0, f"Overall Strength: {strength_rating}") # Add overall strength at the beginning

    return score, feedback

# --- Main execution block ---
if __name__ == "__main__":
    print("Welcome to the Password Complexity Checker!")
    print("------------------------------------------")

    while True:
        password_input = input("Enter a password to check (type 'quit' to exit): ")
        if password_input.lower() == 'quit':
            print("Exiting password checker. Goodbye!")
            break

        score, feedback_messages = check_password_strength(password_input)

        print("\n--- Password Analysis ---")
        print(f"Password: '{password_input}'")
        print(f"Score: {score}/8") # Max score is 3 (length) + 1*4 (char types) = 7. Let's make it 8 total, for future improvements.
        for msg in feedback_messages:
            print(f"- {msg}")
        print("-------------------------\n")
