import tkinter as tk
from tkinter import ttk

class BMI(ttk.Frame):
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.title("BMI calc")
        mainwindow.geometry("400x300")
        mainwindow.configure(bg='blue')
        tk.Label(mainwindow, text="Weight (kg)").grid(row=0, column=0)
        tk.Label(mainwindow, text="Height (m)").grid(row=1, column=0)
        self.weight = tk.Entry(mainwindow)
        self.weight.grid(row=0, column=1)    
        self.height = tk.Entry(mainwindow)
        self.height.grid(row=1, column=1)  
        self.btn = tk.Button(mainwindow, text="Click", command=self.action)
        self.btn.grid(row=2, column=1, columnspan=2,padx= 5,pady=5)
        self.result = tk.Label(mainwindow, text="")
        self.result.grid(row=3, column=0, columnspan=2)
        

    def action(self):
        weight = float(self.weight.get())
        height = float(self.height.get())
        bmi = weight / (height ** 2)
        self.result.config(text=f"Your BMI is: {bmi}")

root = tk.Tk()
exc = BMI(root) 
root.mainloop()
