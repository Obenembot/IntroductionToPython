import tkinter as tk
from tkinter import messagebox

window = tk.Tk()  # Use to Create a Window
window.title("First Desktop Application")  # Use to set a title
label = tk.Label(window, text="First Desktop App in Python")
email = tk.Text(window)
password = tk.Text(window)
placeholder = "Enter your email here..."
email.insert("1.0", placeholder)


#  Method to collect Data
def collect_data():
    user_email = email.get("1.0", tk.END).strip()
    user_password = password.get("1.0", tk.END).strip()
    user_password = password.get("1.0", tk.END).strip()

    if user_email:
        messagebox.showinfo("Collected", f"1. {user_email}\n2. {user_password}")
        print("Inputted Email is ", user_email)
    else:
        messagebox.showwarning("Email is Required", "Please enter email")

    if not user_password:
        messagebox.showwarning("Password is Required", "Please enter password")



def on_focus_in(event):
    if email.get("1.0", tk.END).strip() == placeholder:
        email.delete("1.0", tk.END)
        email.config(fg="black")


def on_focus_out(event):
    if  not email.get("1.0", tk.END).strip():
        email.insert("1.0", placeholder)
        email.config(fg="gray")


button = tk.Button(window, text="Submit", command=collect_data)

label.pack()
email.pack()
password.pack()
button.pack()
# label.grid()

# Configs like styling
label.config(font=("Arial", 16), fg="red", bg="yellow", width=40, height=10)
email.config(font=("Arial", 16), width=30, height=3)
password.config(font=("Arial", 16), width=30, height=3)
button.config(width=20, height=2)

# Bind focus events
email.bind("<FocusIn>", on_focus_in)
email.bind("<FocusOut>", on_focus_out)

window.mainloop()  # Use to Invoke or display
