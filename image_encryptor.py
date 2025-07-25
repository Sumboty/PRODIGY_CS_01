# Task 2: Pixel Manipulation for Image Encryption
# This program performs a very simple pixel-level encryption/decryption
# using the XOR operation with a given key.

from PIL import Image
import os

def encrypt_decrypt_image(image_path, output_path, key, mode):
    """
    Encrypts or decrypts an image using a simple XOR operation on pixel values.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the processed image.
        key (int): An integer key for the XOR operation (0-255 recommended).
        mode (str): 'encrypt' or 'decrypt'.
    """
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Input image '{image_path}' not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Convert image to RGB mode if it's not already (e.g., for PNGs with alpha channel)
    # This ensures we always have 3 color channels (R, G, B) to work with.
    img = img.convert("RGB")
    pixels = img.load() # Load pixel data to manipulate

    width, height = img.size

    print(f"Processing image: {image_path} ({width}x{height} pixels) with key {key} in {mode} mode...")

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y] # Get the RGB tuple for the current pixel

            # Apply XOR operation to each color component
            # Note: XORing with the same key twice reverts the operation,
            # so encryption and decryption use the same logic here.
            processed_r = r ^ key
            processed_g = g ^ key
            processed_b = b ^ key

            pixels[x, y] = (processed_r, processed_g, processed_b) # Set the new pixel value

    try:
        img.save(output_path)
        print(f"Image {'encrypted' if mode == 'encrypt' else 'decrypted'} and saved to: '{output_path}'")
    except Exception as e:
        print(f"Error saving image: {e}")


def get_user_input():
    """
    Gets input from the user for image paths, key, and mode.
    """
    input_image = input("Enter the path to the input image (e.g., image.png): ")
    output_image = input("Enter the path for the output image (e.g., encrypted_image.png): ")

    encryption_key = 0
    while True:
        try:
            # Key should ideally be 0-255 for byte-level operations, but XOR handles overflow
            # We'll stick to 0-255 for simplicity and direct manipulation.
            key_input = int(input("Enter an integer key (0-255 recommended): "))
            if 0 <= key_input <= 255:
                encryption_key = key_input
                break
            else:
                print("Key out of recommended range. Using it anyway, but 0-255 is typical for pixel operations.")
                encryption_key = key_input # Still accept, but warn
                break
        except ValueError:
            print("Invalid input. Please enter an integer for the key.")

    mode_choice = ""
    while True:
        mode_choice = input("Do you want to 'encrypt' or 'decrypt'? ").lower()
        if mode_choice in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

    return input_image, output_image, encryption_key, mode_choice

# --- Main execution block ---
if __name__ == "__main__":
    print("Welcome to the Image Encryption/Decryption Tool!")
    print("-------------------------------------------------")
    print("Note: This uses a simple pixel XOR for educational purposes, NOT for secure encryption.")
    print("-------------------------------------------------")

    input_path, output_path, key, mode = get_user_input()

    encrypt_decrypt_image(input_path, output_path, key, mode)

    print("\nOperation complete.")
