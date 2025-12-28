import tkinter as tk
from tkinter import filedialog

def encrypt():
    file = filedialog.askopenfilename()
    key = 123
    with open(file, "rb") as f:
        data = f.read()
    encrypted = bytes([b ^ key for b in data])
    with open(file, "wb") as f:
        f.write(encrypted)
    status.config(text="File Encrypted/Decrypted")

root = tk.Tk()
root.title("File Encryptor")

tk.Button(root, text="Select File", command=encrypt).pack()
status = tk.Label(root, text="")
status.pack()

root.mainloop()
