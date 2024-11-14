import tkinter as tk
from tkinter import messagebox

'WARNING: Program in Development'
'Error with large decryption tasks... Data Loss likelihood [HIGH]'


def encode_text():
    text = entry_text.get("1.0", tk.END)  # Get all text, including newlines
    key = entry_key.get().strip()
    if not text or not key.isdigit():
        messagebox.showwarning("Input Error", "Please enter text and a valid numeric key.")
        return

    # Display warning if text length exceeds 300 characters
    if len(text) > 250:
        label_warning.config(text="Warning: Data loss may occur for characters > 250.", fg="red")
    else:
        label_warning.config(text="")  # Clear warning if text is below 300 characters

    key = int(key)
    encoded_chars = [chr((ord(char) + key) % 128) for char in text if ord(char) < 128]  # ASCII encoding only
    encoded_text = ''.join(encoded_chars)

    entry_text.delete("1.0", tk.END)
    entry_text.insert("1.0", encoded_text)
    messagebox.showinfo("Success", "Text encoded successfully.")


def decode_text():
    text = entry_text.get("1.0", tk.END)  # Get all text, including newlines
    key = entry_key.get().strip()
    if not text or not key.isdigit():
        messagebox.showwarning("Input Error", "Please enter encoded text and a valid numeric key.")
        return

    # Display warning if text length exceeds 300 characters
    if len(text) > 300:
        label_warning.config(text="Warning: Data loss may occur for characters > 300.", fg="red")
    else:
        label_warning.config(text="")  # Clear warning if text is below 300 characters

    key = int(key)
    decoded_chars = [chr((ord(char) - key) % 128) for char in text if ord(char) < 128]  # ASCII decoding only
    decoded_text = ''.join(decoded_chars)

    entry_text.delete("1.0", tk.END)
    entry_text.insert("1.0", decoded_text)
    messagebox.showinfo("Success", "Text decoded successfully.")


# Setting up the GUI
root = tk.Tk()
root.title("ASCII Text Encoder/Decoder")

# Text entry
label_text = tk.Label(root, text="Enter Text:")
label_text.pack(padx=10, pady=5)
entry_text = tk.Text(root, height=10, width=50, bd=2, relief="solid")
entry_text.pack(padx=10, pady=5)

# Key entry
label_key = tk.Label(root, text="Enter Key (numeric):")
label_key.pack(padx=10, pady=5)
entry_key = tk.Entry(root, bd=2, relief="solid")
entry_key.pack(padx=10, pady=5)

# Warning Label
label_warning = tk.Label(root, text="", fg="red")
label_warning.pack(padx=10, pady=5)

# Encode and Decode buttons
button_encode = tk.Button(root, text="Encode", command=encode_text, bd=2, relief="solid")
button_encode.pack(pady=5)

button_decode = tk.Button(root, text="Decode", command=decode_text, bd=2, relief="solid")
button_decode.pack(pady=5)

# Run the main event loop
root.mainloop()
