import tkinter as tk

class greetapp:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow
        mainwindow.geometry("300x200")
        mainwindow.title("Greeting App")

        tk.Label(mainwindow,text="Enter Your Name").pack()


        #ADD widget
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.btn = tk.Button(mainwindow,text="Enter",command=self.action)
        self.btn.pack()
        self.outLabel = tk.Label(mainwindow,text="",fg="red")
        self.outLabel.pack()
    def action(self):
        data = self.name_entry.get()
        self.outLabel.config(text='Hello, ' +data)
        self.name_entry.delete(0, tk.END)

        
#main code
root =tk.Tk()
exc = greetapp(root) 
root.mainloop()
