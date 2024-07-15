import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

def convert():
    try:
        one = name1.get()
        two = name2.get()
        firstAmount = entry1.get()

        if not one or not two or not firstAmount:
            messagebox.showerror("Error","There is some problem")
        else:
            baseAmount1 = data[one]
            baseAmount2 = data[two]

            answer = float( (float(firstAmount)*float(baseAmount2))/float(baseAmount1) )
            
            entry2.delete(0 , tk.END)
            entry2.insert(0 , str(round(answer , 5)) + " " + str(two))
    except:
        messagebox.showerror("Error","There is some problem")

items = {
    "INR": "Indian Rupees",
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "BRL": "Brazilian Real"
}

data = {
    "INR":1.00,
    "USD":0.012,
    "EUR":0.011,
    "GBP":0.0094,
    "JPY":1.90,
    "AUD":0.018,
    "CAD":0.017,
    "CHF":0.016,
    "CNY":0.087,
    "BRL":0.065
}

keys = data.keys()
keys = list(keys)

base = tk.Tk()
base.title("Currency Converter")
base.geometry("400x500")

nb = Notebook(base)

frame = Frame(nb)

label = Label(frame , text="Select appropriate options" , font=("Arial",15))
label.grid(row=0 , column=0 , columnspan=2 , pady=20)

name1 = Combobox(frame , values=keys)
name1.set("Select :")
name1.grid(row = 1 , column = 1 , padx=15)

entry1 = Entry(frame , width=15 , font=("Arial" , 12))
entry1.grid(row=1 , column=0 , pady=20 , padx=15)

name2 = Combobox(frame , values=keys)
name2.set("Select :")
name2.grid(row = 2 , column = 1 , padx=15)

entry2 = Entry(frame , width=15, font=("Arial" , 12) )
entry2.grid(row=2 , column=0 , pady=20 , padx=15)

button = Button(frame , text="Convert" , command= lambda : convert())
button.grid(row=3 , column=1 , pady=10)

actualLabel = Label(frame , text="Currency" , font=("Arial" , 15))
actualLabel.grid(row=4 , column=0 , columnspan=2)

listBox = tk.Listbox(frame , width=50)
for item in keys:
    listBox.insert(tk.END , f"{item} : {items[item]}")
listBox.grid(row=5 , column=0 , columnspan=2 , padx=10)

frame.pack(fill=tk.BOTH , expand=True)

nb.pack(fill=tk.BOTH , expand=True , padx=20 , pady=10)
nb.add(frame , text="Converter")

base.mainloop()