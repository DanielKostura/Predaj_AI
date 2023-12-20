import datetime as dt
import tkinter as tk
from tkinter import *

def date():
    current_time = dt.date.today() + dt.timedelta(days=d)
    current_time = current_time.strftime("%d.%m.%Y")
    p.create_rectangle(0, 0, 450, 40, fill="orange", outline="orange")
    p.create_text(450/2, 20, text=current_time, font=('Times New Roman', 15))

def branko(sopkovica):
    pass

def risko():
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
    global dnes
    dnes = True
    draw()

def yesterday():
    global dnes
    dnes = False
    draw()

def sopkovica():
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_sopkovica = int(lines[0]) + 1
        lines[0] = str(count_sopkovica) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def rum():
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_rum = int(lines[1]) + 1
        lines[1] = str(count_rum) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def punc():
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_punc = int(lines[2]) + 1
        lines[2] = str(count_punc) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def medova():
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_medova = int(lines[3]) + 1
        lines[3] = str(count_medova) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def cervene_vinko():
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_cervene_vinko = int(lines[4]) + 1
        lines[4] = str(count_cervene_vinko) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def draw():
    p.delete("all")
    date()

    global dnes
    
    if dnes == True:
        with open("today.txt", "r") as read:
            lines = read.readlines()
    else:
        with open("yesterday.txt", "r") as read:
            lines = read.readlines()

    sum = 0
    for i in range(5):
        lines[i] = int(lines[i])
        sum += lines[i]
    
    if sum == 0:
        sum = 1

    for i in range(5):
        p.create_rectangle(W/5*i+5, H-80, W/5*i+80, H-80 - lines[i]/sum * 200, fill="blue")
        p.create_text(40+90*i, 535, text=str(lines[i]))

def optional_buttons():
    b1 = Button(o, text="Nový deň", command=new_day, width=63, height=2)
    b1.place(x=1, y=40)

    b2 = Button(o, text="Dnešný predaj", command=today, width=63, height=2)
    b2.place(x=1, y=40*2)

    b3 = Button(o, text="Včerajší predaj",command=yesterday, width=63, height=2)
    b3.place(x=1, y=40*3)

    b4 = Button(o, text="Koniec", command=o.destroy, width=63, height=2)
    b4.place(x=1, y=40*4)

def alko_buttons():
    b1 = Button(o, text="Sopkovica",fg='white',command=sopkovica,bg='black', width=11, height=2)
    b1.place(x=W/5*0+5, y=H-40)

    b2 = Button(o, text="Rum",command=rum,bg='#8C4103', width=10, height=2)
    b2.place(x=W/5*1+5, y=H-40)

    b3 = Button(o, text="Punč",command=punc,bg='dark red', width=10, height=2)
    b3.place(x=W/5*2+5, y=H-40)

    b4 = Button(o, text="Medová 14°",command=medova,bg='yellow', width=10, height=2)
    b4.place(x=W/5*3+5, y=H-40)

    b5 = Button(o, text="Červené vínko",command=cervene_vinko,bg='red', width=10, height=2)
    b5.place(x=W/5*4+5, y=H-40)

def menu():
    date()
    draw()
    alko_buttons()
    optional_buttons()

W = 450
H = 600
o = Tk()
o.title("Usmej sa :)")
p = tk.Canvas(width=W, height=H)
p.pack()

d = 0
dnes = True

menu()
p.mainloop()