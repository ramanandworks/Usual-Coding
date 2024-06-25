import tkinter as tk
from tkinter import messagebox
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter numeric values.")
        return

    operation = operation_var.get()

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)
    else:
        messagebox.showerror("Operation Error", "Please select a valid operation.")
        return

    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Basic Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="Add")
operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()