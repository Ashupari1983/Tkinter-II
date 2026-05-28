from tkinter import *

window = Tk()
window.title("Main Window")
window.geometry('400x400')

def topwin():
    top = Toplevel()
    top.title("Top Window")
    top.geometry('200x200')

    l = Label(top, text = 'This is the toplevel window.' )
    l.pack()

    top.mainloop()

l1 = Label(text = "This is the main window.")
b1 = Button(text="Click to open Top window.", command = topwin, bg = "light pink")
l1.pack()
b1.pack()
window.mainloop()