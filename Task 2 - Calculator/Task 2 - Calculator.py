import tkinter as tk
from tkinter import messagebox

# Global state
current_result = None
history_entries = []

def calculate(operation):
    global current_result

    try:
        num1_text = entry1.get()
        num2_text = entry2.get()

        # Prioritize using previous result if present
        if current_result is not None and num1_text == "":
            num1 = current_result
        else:
            num1 = float(num1_text)

        num2 = float(num2_text)

        if operation == "Add":
            result = num1 + num2
            expression = f"{num1} + {num2} = {result}"
        elif operation == "Subtract":
            result = num1 - num2
            expression = f"{num1} - {num2} = {result}"
        elif operation == "Multiply":
            result = num1 * num2
            expression = f"{num1} * {num2} = {result}"
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
            expression = f"{num1} / {num2} = {result}"
        else:
            raise ValueError("Unknown operation.")

        current_result = result
        result_label.config(text=f"Result: {result}")
        history_entries.append(expression)
        update_history()

        # Clear only second entry (allow chaining from first or result)
        entry2.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

def update_history():
    history_text.config(state='normal')
    history_text.delete(1.0, tk.END)
    for entry in history_entries:
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state='disabled')

def reset():
    global current_result, history_entries
    current_result = None
    history_entries = []
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    update_history()

# Main window
root = tk.Tk()
root.title("Cumulative Calculator")
root.geometry("550x600")
root.configure(bg="black")

# Entry fields
tk.Label(root, text="Enter first number:", bg="black", fg="white").pack(pady=5)
entry1 = tk.Entry(root, bg="black", fg="white")
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="black", fg="white").pack(pady=5)
entry2 = tk.Entry(root, bg="black", fg="white")
entry2.pack(pady=5)

# Operation buttons
tk.Label(root, text="Choose Operation:", bg="black", fg="white").pack(pady=5)
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

operations = ["Add", "Subtract", "Multiply", "Divide"]
for op in operations:
    btn = tk.Button(button_frame, text=op,
                    command=lambda o=op: calculate(o),
                    bg='yellow', fg='black', relief='flat', width=10)
    btn.pack(pady=2)

# Reset Button
tk.Button(root, text="Reset", command=reset,
          bg="red", fg="white", relief='flat', width=10).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", bg="black", fg="white")
result_label.pack(pady=10)

# History panel
history_frame = tk.Frame(root, bg="black")
history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

tk.Label(history_frame, text="History", bg="black", fg="white").pack()

history_text = tk.Text(history_frame, width=25, height=20, bg="black", fg="white", state='disabled')
history_text.pack(pady=5)

root.mainloop()
