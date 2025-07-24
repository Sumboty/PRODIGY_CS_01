# Task 1: Caesar Cipher Implementation
# This program encrypts and decrypts text using the Caesar Cipher algorithm.

def get_user_input():
    """
    Prompts the user for the message, shift value, and mode (encrypt/decrypt).
    Includes input validation.
    """
    message = input("Enter your message: ")

    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break  # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")

    while True:
        mode = input("Do you want to 'encrypt' or 'decrypt'? ").lower()
        if mode in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
    return message, shift, mode

def caesar_cipher_process(text, shift, mode):
    """
    Performs Caesar Cipher encryption or decryption on the given text.

    Args:
        text (str): The input message to process.
        shift (int): The number of positions to shift characters.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The processed message.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            start_ascii = 0
            if char.islower():
                start_ascii = ord('a')
            else:  # char.isupper()
                start_ascii = ord('A')

            # Convert character to a 0-25 index (0 for 'a'/'A', 25 for 'z'/'Z')
            char_index = ord(char) - start_ascii

            shifted_index = 0
            if mode == 'encrypt':
                # Apply shift, then use modulo 26 to wrap around the alphabet
                shifted_index = (char_index + shift) % 26
            elif mode == 'decrypt':
                # For decryption, we effectively shift backwards.
                # Adding 26 before modulo handles negative results correctly.
                shifted_index = (char_index - shift + 26) % 26

            # Convert the new index back to an ASCII value and then to a character
            shifted_char = chr(start_ascii + shifted_index)
            result += shifted_char
        else:
            # If it's not an alphabet character (e.g., space, number, symbol), keep it as is
            result += char
    return result

# --- Main execution block ---
if __name__ == "__main__":
    print("Welcome to the Caesar Cipher Tool!")
    print("----------------------------------")

    message, shift, mode = get_user_input()

    processed_message = caesar_cipher_process(message, shift, mode)

    print("\n--- Results ---")
    print(f"Original Message: '{message}'")
    print(f"Shift Value: {shift}")
    print(f"Mode Selected: {mode.capitalize()}")
    print(f"Processed Message: '{processed_message}'")
    print("----------------------------------")
