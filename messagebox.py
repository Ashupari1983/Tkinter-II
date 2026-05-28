from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Checker")
window.geometry('400x400')

def a():
    messagebox.askyesnocancel("Warning!", "Virsus has been found.")

b1 = Button(text = 'Check for Virus', width=40, bg = "light pink", relief = RAISED, bd =4, command = a)
b1.place(x = 200, y =200)
window.mainloop()