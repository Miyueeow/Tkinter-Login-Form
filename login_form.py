import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "1234":
        status_label.config(text="Login successful", fg="green")
    else:
        status_label.config(text="Incorrect credentials", fg="red")

def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    status_label.config(text="")

# Create the main application window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, padx=10, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
