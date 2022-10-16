import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import keyboard
import time
import generate
import main

#create window
window = tk.Tk()
window.title('TYPE.ai')
window.resizable(0,0)

window.geometry("600x300")

x = 0

x1 = tk.Label(window, text = "type bitch", font = "Arial 20")
x1.place(x=10, y=50)

def game():
    global X
    if x == 0:
        x = 1
        window.destroy()

    words = main.get_diagnose()

    #Create new window
    windows = tk.Tk()
    windows.title("TYPE.ai")
    windows.configure(bg="Aquamarine")
    windows.geometry("850x400")


submit = tk.Button(window, text="Submit", command=game, width=12, bg='white', fg="tomato", font="Algerian 10")
submit.place(x=150, y=100)


window.mainloop()