import random
import string
import tkinter as tk
from tkinter import messagebox, ttk


def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than zero.")

        # Build the character set based on user choices
        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        # Check if the user selected at least one character type
        if not characters:
            raise ValueError("Please select at least one character type.")

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the password
        output_label.config(text=password)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.configure(bg="#2C2C2C")  # Charcoal background

# Font settings
font_title = ("Roboto Mono", 14, "bold")
font_normal = ("Roboto Mono", 12)
font_output = ("Roboto Mono", 16, "bold")

# Style configuration for ttk widgets
style = ttk.Style()
style.theme_use("default")
style.configure("Custom.TCheckbutton",
                font=font_normal,
                background="#2C2C2C",
                foreground="white",
                focuscolor="#2C2C2C",
                indicatorcolor="white",
                indicatorbackground="#4CAF50")  # Green focus when selected

# Password Length Input
tk.Label(root, text="Enter Password Length:", font=font_title, fg="white", bg="#2C2C2C").pack(pady=10)
length_entry = tk.Entry(root, font=font_normal, bg="white", fg="black")
length_entry.pack(pady=5)

# Checkboxes for character options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

ttk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, style="Custom.TCheckbutton").pack(
    anchor="center", pady=5)
ttk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, style="Custom.TCheckbutton").pack(
    anchor="center", pady=5)
ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var, style="Custom.TCheckbutton").pack(anchor="center",
                                                                                                      pady=5)
ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var, style="Custom.TCheckbutton").pack(anchor="center",
                                                                                                      pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=font_title, bg="#4CAF50",
                            fg="white", activebackground="#45A049")
generate_button.pack(pady=20)

# Output Label for Generated Password
output_label = tk.Label(root, text="", font=font_output, fg="white", bg="#2C2C2C", wraplength=450, justify="center")
output_label.pack(pady=10)

# Run the GUI
root.mainloop()



