from tkinter import *
import random

root = Tk()
root.title("Dice simulator")


l1 = Label(root,font=("Helvitica",200,'bold'),text="")

def rolldice():
    
    number=['\u2680','\u2681','\u2682','{random.ch\u2683','\u2684','\u2685']
    l1.configure(text=f'{random.choice(number)}')
    l1.pack()

button = Button(root,font=("Helvitica", 50 , 'bold'), text = "Dice roll", command = rolldice, bg = 'lightblue', fg = 'red')
button.pack()

root.mainloop()
