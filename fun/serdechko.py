import tkinter as tk

def click(btn_text):
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row, col = 1, 0
for btn_text in buttons:
    action = lambda x=btn_text: click(x)
    tk.Button(root, text=btn_text, width=5, height=2, font=("Arial", 16), command=action)\
        .grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()