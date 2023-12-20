import datetime as dt
import tkinter as tk
from tkinter import *

def date():
    current_time = dt.date.today() + dt.timedelta(days=d)
    current_time = current_time.strftime("%d.%m.%Y")
    p.create_rectangle(0, 0, 450, 40, fill="orange", outline="orange")
    p.create_text(450/2, 20, text=current_time, font=('Times New Roman', 15))

def branko():
    pass

def drunk_branko():
    pass

def risko():
    pass

def drunk_risko():
    pass

def new_day():
    global d
    d += 1
    date()

    with open("today.txt", "r") as today:
        with open("yesterday.txt", "w") as yesterday:
            for line in today:
                print(line.strip(), file=yesterday)
    
    with open("today.txt", "w") as today:
        print(0, file=today)
        print(0, file=today)
        print(0, file=today)
        print(0, file=today)
        print(0, file=today)

def today():
    with open("today.txt", "r") as f:
        sopkovica = int(f.readline())
        rum = int(f.readline())
        punc = int(f.readline())
        medova = int(f.readline())
        cervene_vinko = int(f.readline())

        print(sopkovica)
        print(rum)
        print(punc)
        print(medova)
        print(cervene_vinko)

def yesterday():
    with open("yesterday.txt", "r") as f:
        sopkovica = int(f.readline())
        rum = int(f.readline())
        punc = int(f.readline())
        medova = int(f.readline())
        cervene_vinko = int(f.readline())

        print(sopkovica)
        print(rum)
        print(punc)
        print(medova)
        print(cervene_vinko)

def optional_buttons():
    b1 = Button(o, text="Nový deň", command=new_day, width=63, height=2)
    b1.place(x=1, y=40)

    b2 = Button(o, text="Dnešný predaj zmrzliny", command=today, width=63, height=2)
    b2.place(x=1, y=40*2)

    b3 = Button(o, text="Včerajší predaj zmrzliny",command=yesterday, width=63, height=2)
    b3.place(x=1, y=40*3)

    b4 = Button(o, text="Koniec", command=o.destroy, width=63, height=2)
    b4.place(x=1, y=40*4)

def alko_buttons():
    b1 = Button(o, text="Sopkovica", width=11, height=2)
    b1.place(x=W/5*0+5, y=H-40)

    b2 = Button(o, text="Rum", width=10, height=2)
    b2.place(x=W/5*1+5, y=H-40)

    b3 = Button(o, text="Punč", width=10, height=2)
    b3.place(x=W/5*2+5, y=H-40)

    b4 = Button(o, text="Medová 14°", width=10, height=2)
    b4.place(x=W/5*3+5, y=H-40)

    b5 = Button(o, text="Červené vínko", width=10, height=2)
    b5.place(x=W/5*4+5, y=H-40)

def menu():
    date()
    alko_buttons()
    optional_buttons()

W = 450
H = 600
o = Tk()
o.title("Usmej sa :)")
p = tk.Canvas(width=W, height=H)
p.pack()
d = 0

menu()

p.mainloop()