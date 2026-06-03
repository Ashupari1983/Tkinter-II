from tkinter import *
import random

window = Tk()
window.title("Rock Paper Scissors")

l1 = Label(text = 'Enter your move (rock, paper or scissors):')
e1 = Entry(bd = 3, relief = SUNKEN)
t1 = Text()

def move():
    lst = ['rock','paper','scissors']
    a = random.choice(lst)
    t1.insert(END,"\nComputer's choice: " + a + "\n")
    b = e1.get().lower()
    
    if a == b:
        t1.insert(END, "It's a tie!")
    elif a == 'rock' and b == 'paper' or a == 'paper' and b == 'scissors' or a == 'scissors' and b == 'rock':
        t1.insert(END, "You win!")
    elif a == 'rock' and b == 'scissors' or a == 'paper' and b == 'rock' or a == 'scissors' and b == 'paper':
        t1.insert(END, "You lose!")   

b1 = Button(text = "Click to finalize and see computer's move", relief = RAISED, command = move)

l1.pack()
e1.pack()
b1.pack()
t1.pack()

window.mainloop()