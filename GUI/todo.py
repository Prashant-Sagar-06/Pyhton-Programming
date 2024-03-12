import tkinter as tk

class TODO():
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.title("TODO List")
        mainwindow.geometry("400x300")
        tk.Label(mainwindow, text="Enter Task").grid(row=0, column=0)
        self.task = tk.Entry(mainwindow)
        self.task.grid(row=0, column=1) 
        self.btn = tk.Button(mainwindow, text="Add task", command=self.additem) 
        self.btn.grid(row=0, column=2, columnspan=4, padx=5, pady=5)
        self.list_box = tk.Listbox(mainwindow, width=40, bg="grey", border=2)
        self.list_box.grid(row=1, columnspan=2)

        self.bt_delete = tk.Button(mainwindow, text="Delete item", command=self.delete_item)
        self.bt_delete.grid(row=2, column=0)

        self.bt_delete_all = tk.Button(mainwindow, text="Delete All item", command=self.delete_all_items)
        self.bt_delete_all.grid(row=2, column=1)

        self.bt_undo = tk.Button(mainwindow, text="undo", command=self.undo)
        self.bt_undo.grid(row=2, column=2)

        self.deleted_items = []

    def additem(self):
        data = self.task.get()
        self.list_box.insert(tk.END, data)
        self.task.delete(0, tk.END)

    def delete_item(self):
            index = self.list_box.curselection()[0]
            
            self.deleted_items.append((index, self.list_box.get(index)))
            self.list_box.delete(index)
        

    def delete_all_items(self):
        for i in self.list_box.get(0, tk.END):
            self.deleted_items.append(i)
        self.list_box.delete(0, tk.END)

    def undo(self):
        for i in self.deleted_items:
            self.list_box.insert(1, i)
        self.delete_item.clear()

root = tk.Tk()
exc = TODO(root) 
root.mainloop()
