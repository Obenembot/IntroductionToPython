import tkinter as tk

# Create window
window = tk.Tk()
window.title("Entry and Listbox Example")

# Entry widget (for input)
entry = tk.Entry(window, width=40, font=("Arial", 14))
entry.pack(pady=10)

# Listbox (to display added items)
listbox = tk.Listbox(window, width=40, height=6, font=("Arial", 14))
# listbox.pack(pady=10)
listbox.pack(pady=10)

# Function to add entry text to listbox
def add_item():
    item = entry.get().strip()
    if item:
        listbox.insert(tk.END, item)  # add to bottom
        entry.delete(0, tk.END)       # clear entry field

# Button to add items
add_button = tk.Button(window, text="Add to List", command=add_item, width=20, height=2)
add_button.config(fg="red", bg="yellow")
add_button.pack(pady=5)

# Run app

frame = tk.Frame(window)
frame.pack()

btn1 = tk.Button(frame, text="OK")
btn2 = tk.Button(frame, text="Cancel")
btn1.pack(side="left")
btn2.pack(side="left")


window.mainloop()


