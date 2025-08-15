import tkinter as tk

# Function to update expression
def press (num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total) 
        expression = total      
    except:
        equation.set("Error")
        expression = ""

# Function to clear display
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("tkinter Calculator")
root.geometry("300x350")

expression = ""
equation = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=equation, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=5)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=equalpress)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()