import tkinter as tk

class PatternMaker:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.geometry("300x200")
        mainwindow.title("Pattern Maker")

        tk.Label(mainwindow, text="Enter the number of rows").pack()

        # ADD WIDGET
        self.number_entry = tk.Entry(mainwindow)
        self.number_entry.pack()

        self.btn1 = tk.Button(mainwindow, text="Generate", command=self.generate_pattern)
        self.btn1.pack()

        self.result_label = tk.Label(mainwindow, text="")
        self.result_label.pack()

    # ACTION
    def generate_pattern(self):
        n = int(self.number_entry.get())
        pattern = self.triangle_pattern(n)
        self.result_label.config(text=pattern)

    
    def triangle_pattern(self,n):
        pattern = ""
        for i in range(1, n+1):
            pattern += ' ' * (n - i) + '*' * (2 * i - 1) + '\n'
        return pattern


# main code
root = tk.Tk()
exc = PatternMaker(root)
root.mainloop()
