import tkinter as tk
from tkinter import messagebox
import base64


# Program Designed for basic encryption of generated authentication tables.
#CAUTION: Basic Encryption method in use, Ensure secure data transfer!


# Function to encrypt text
def encrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            raise ValueError("No text provided for encryption.")
        # Encode the text using Base64
        encrypted_bytes = base64.b64encode(text.encode("utf-8"))
        encrypted_text = encrypted_bytes.decode("utf-8")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decrypt text
def decrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            raise ValueError("No text provided for decryption.")
        # Decode the text using Base64
        decrypted_bytes = base64.b64decode(text.encode("utf-8"))
        decrypted_text = decrypted_bytes.decode("utf-8")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input for decryption.")

# Set up the main application window
root = tk.Tk()
root.title("Base64 Encryption Tool")
root.geometry("400x300")

# Input Label
input_label = tk.Label(root, text="Input Text")
input_label.pack()

# Input Text Area
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

# Decrypt Button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

# Output Label
output_label = tk.Label(root, text="Output Text")
output_label.pack()

# Output Text Area
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Run the application
root.mainloop()
