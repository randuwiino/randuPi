import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

import random

Root = tk.Tk()
Root.withdraw()

answer = simpledialog.askinteger(title="Password", prompt="Guess a number from 1 to 9:")
print(type(answer))
random = random.randint(1,9)
print(type(random))

while (answer != random):

    if answer >= 10:
        
        print(messagebox.showinfo("Dumb Ass", "Haya, I said choose number between 1 to 9 la!"))
        answer = simpledialog.askinteger(title="Answer", prompt="Guess a number from 1 to 9:")
        
    elif answer <= 10:
        print(messagebox.showinfo("Dimwit", "Haya, try harder la!"))
        answer = simpledialog.askinteger(title="Answer", prompt="Guess a number from 1 to 9:")

print(messagebox.showinfo("Finally", "So koot la, the answer is " + str(random)))