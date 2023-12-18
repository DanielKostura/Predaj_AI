import datetime as dt
import tkinter as tk
from tkinter import *

def date():
    current_time = dt.datetime.now().strftime("%d.%m.%Y")
    p.create_rectangle(0, 0, 450, 40, fill="orange", outline="orange")
    p.create_text(450/2, 20, text=current_time, font=('Times New Roman', 15))

def optional_buttons():
    b1 = Button(o, text="Nový deň", width=63, height=2)
    b1.place(x=1, y=40)

    b2 = Button(o, text="Dnešný predaj zmrzliny", width=63, height=2)
    b2.place(x=1, y=40*2)

    b3 = Button(o, text="Včerajší predaj zmrzliny", width=63, height=2)
    b3.place(x=1, y=40*3)

    b4 = Button(o, text="Koniec", width=63, height=2)
    b4.place(x=1, y=40*4)

def alko_buttons():
    b1 = Button(o, text="Punč", width=11, height=2)
    b1.place(x=W/5*0+5, y=H-40)

    b2 = Button(o, text="Vínko", width=10, height=2)
    b2.place(x=W/5*1+5, y=H-40)

    b3 = Button(o, text="Sopkovica", width=10, height=2)
    b3.place(x=W/5*2+5, y=H-40)

    b4 = Button(o, text="Borovička", width=10, height=2)
    b4.place(x=W/5*3+5, y=H-40)

    b5 = Button(o, text="Sopkovica", width=10, height=2)
    b5.place(x=W/5*4+5, y=H-40)


def persons():
    pass

def menu():
    date()
    alko_buttons()
    optional_buttons()

W = 450
H = 600
o = Tk()
p = tk.Canvas(width=W, height=H)
p.pack()

menu()
"""
p.create_rectangle(0, 560, 450/5, 600, fill="green", outline="green")
p.create_rectangle(450/5, 560, 450/5*2, 600, fill="red", outline="red")
p.create_rectangle(450/5*2, 560, 450/5*3, 600, fill="pink", outline="pink")
p.create_rectangle(450/5*3, 560, 450/5*4, 600, fill="purple", outline="purple")
p.create_rectangle(450/5*4, 560, 450, 600, fill="yellow", outline="yellow")
"""

p.mainloop()
