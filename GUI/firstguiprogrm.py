# GUI ==>>> GRAPHICAL USER INTERFACE
# import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('200x100')
root.title('COUNTER APP')
root.minsize(100,50)

#global initialization
var= IntVar()

#actions

def my_fun1():
    lb.config(text=lb.cget('text')+1)
def my_fun2():
    if lb.cget("text")!=0:
        return  lb.config(text=lb.cget('text')-1)
    else:
        return 0
    
lb = Label(root , text=0,font=("bold",30))
lb.pack()
bt1 = Button(root , text='Increment' , command=my_fun1)
bt1.pack(side=RIGHT,ipadx=10,ipady=10,padx=10,pady=10)
bt2 = Button(root , text='Decrement' , command=my_fun2)
bt2.pack(side=LEFT,ipadx=10,ipady=10,padx=10,pady=10)

root.mainloop()