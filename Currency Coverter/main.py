import requests
import tkinter as tk
from tkinter import ttk, messagebox


# Function to get all currency codes
def get_currency_list():
    try:
        url= "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return list(data['rates'].keys())   # Return all currency codes
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error! Please check internet connection.")
        return []
    
# Function to get exchange rates for base currency
def get_rates(base):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["rates"]
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error! Please Check internet connection.")
        return None
    
# Convert function
def convert_currency():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")
        return
    
    base = base_currency.get()
    target = target_currency.get()

    rates = get_rates(base)
    if rates and target in rates:
        converted = amount * rates[target]
        result_label.config(text=f"{amount} {base} = {converted:.2f} {target}")
    else:
        messagebox.showerror("Error", "Invalid currency code or API error.")

# Main Window
root = tk.Tk()
root.title("Currency Converted - Advanced")
root.geometry("450x350")
root.config(bg="#f2f2f2")

# Title Label
title = tk.Label(root, text="💱 Currency Conveter", font=('Arial', 18, 'bold'), bg="#f2f2f2", fg='#333')
title.pack(pady=10)

# Fetch currency list for dropdown
currency_list = get_currency_list()
if not currency_list:
    root.destroy()
    exit()

#Base Currency
tk.Label(root, text="From Currency:", bg="#f2f2f2").pack()
base_currency = ttk.Combobox(root, values=currency_list, state="readonly", width=15)
base_currency.pack()
base_currency.set("USD")

# Target Currency
tk.Label(root, text="To Currency:", bg="#f2f2f2").pack()
target_currency = ttk.Combobox(root, values=currency_list, state="readonly", width=15)
target_currency.pack()
target_currency.set("INR")

# Amount Entry
tk.Label(root, text="Amount:", bg="#f2f2f2").pack()
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()

# Convert Button
convert_btn = tk.Button(root, text='Convert', command=convert_currency, bg="#4CAF50", fg="white", font=("Arial", 12))
convert_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f2f2f2", fg="#333")
result_label.pack(pady=5)

root.mainloop()