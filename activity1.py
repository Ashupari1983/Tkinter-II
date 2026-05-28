from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Image')
window.geometry('400x400')

upload = Image.open('abc.jpg')
image = ImageTk.PhotoImage(upload)

l1 = Label(image = image, height = 300, width = 350)
l1.place(x=50, y = 10)

l2 = Label(text = "Image")
l2.place(x = 70, y=320)

window.mainloop()