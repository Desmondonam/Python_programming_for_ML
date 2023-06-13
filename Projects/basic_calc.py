# This is a basic calculator application in tkinter
# imprt the tkinter library
import tkinter as tk
# Create the main window of the application
root = tk.Tk()
root.title("Basic Calculator")
# create a text entry field
entry = tk.Entry(root, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)
# create a button click function


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


# create the numerical buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_index = 1
col_index = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=10, pady=10,
                    command=lambda button=button: button_click(button))
    btn.grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1
# create clear button and function


def clear():
    entry.delete(0, tk.END)


clear_button = tk.Button(root, text="Clear", padx=10, pady=10, command=clear)
clear_button.grid(row=row_index, column=col_index)

# create the calculator function


def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


equal_button = tk.Button(root, text="=", padx=10, pady=10, command=calculate)
equal_button.grid(row=row_index, column=col_index)

# run the application

root.mainloop()
