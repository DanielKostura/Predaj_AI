import datetime as dt
import tkinter as tk
from tkinter import *

def date():
    current_time = dt.date.today() + dt.timedelta(days=d)
    current_time = current_time.strftime("%d.%m.%Y")
    p.create_rectangle(0, 0, 450, 40, fill="orange", outline="orange")
    p.create_text(450/2, 20, text=current_time, font=('Times New Roman', 15))

def text():
    global dnes

    sum = 0
    if dnes == True:
        with open("today.txt", "r") as read:
            lines = read.readlines()
    
    elif dnes == False:
        with open("yesterday.txt", "r") as read:
            lines = read.readlines()
    # 1 text
    metanol = int(lines[0])*5*1 # mnozstvo alkoholu * % alkoholu v tom
    etanol = int(lines[1])*5*0.375 + int(lines[2])*3*0.1 + int(lines[3])*50*0.14 + int(lines[4])*2*0.11 # mnozstvo alkoholu * % alkoholu v tom
    etanol = round(etanol, 2)

    p.create_text(450/4, 40*5.5, text=f"Predaný etanol: {etanol}(dl)", font=("Arial", 15))
    p.create_text(450/4*3, 40*5.5, text=f"Predaný metanol: {metanol}(dl)", font=("Arial", 15))

    # 2 text
    max = 0
    for i in range(5):
        sum += int(lines[i])
        if int(lines[i]) > max:
            max = int(lines[i])
    
    p.create_text(450/2, 40*6.5, text=f"Dnes sa predalo {sum} nápojov.", font=("Arial", 15))

    # 3 text
    nums = []
    drink = []
    for i in range(5):
        if int(lines[i]) == max:
            nums.append(i)
    
    for i in nums:
        if i == 0:
            drink.append("Spokovica")
        elif i == 1:
            drink.append("Rum")
        elif i == 2:
            drink.append("Punč")
        elif i == 3:
            drink.append("Medová 14°")
        elif i == 4:
            drink.append("Červené vínko")

    if len(drink) == 1:
        p.create_text(450/2, 40*7.5, text=f"Obľubený nápoj: {drink[0]}", font=("Arial", 15))
    elif len(drink) == 2:
        p.create_text(450/2, 40*7.5, text=f"Obľubené nápoje: {drink[0]}, {drink[1]}", font=("Arial", 15))
    elif len(drink) == 3:
        p.create_text(450/2, 40*7.5, text=f"Obľubené nápoje: {drink[0]}, {drink[1]},", font=("Arial", 15))
        p.create_text(450/2, 40*8.5, text=f"{drink[2]}", font=("Arial", 15))
    elif len(drink) == 4:
        p.create_text(450/2, 40*7.5, text=f"Obľubené nápoje: {drink[0]}, {drink[1]},", font=("Arial", 15))
        p.create_text(450/2, 40*8.5, text=f"{drink[2]}, {drink[3]}", font=("Arial", 15))

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
    
    draw()

def today():
    global dnes
    dnes = True
    draw()

def yesterday():
    global dnes
    dnes = False
    draw()

def sopkovica():
    global dnes

    if dnes == False:
        return
    
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_sopkovica = int(lines[0]) + 1
        lines[0] = str(count_sopkovica) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def rum():
    global dnes

    if dnes == False:
        return
    
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_rum = int(lines[1]) + 1
        lines[1] = str(count_rum) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def punc():
    global dnes

    if dnes == False:
        return
    
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_punc = int(lines[2]) + 1
        lines[2] = str(count_punc) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def medova():
    global dnes

    if dnes == False:
        return
    
    with open("today.txt", "r") as read:
        lines = read.readlines()
        count_medova = int(lines[3]) + 1
        lines[3] = str(count_medova) + "\n"
    
    with open("today.txt", "w") as write:
        for i in range(5):
            print(lines[i], end="", file=write)

    draw()

def cervene_vinko():
    global dnes

    if dnes == False:
        return
    
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
    text()

    global dnes
    
    if dnes == True:
        with open("today.txt", "r") as read:
            lines = read.readlines()
    else:
        with open("yesterday.txt", "r") as read:
            lines = read.readlines()

    sum = 0
    max_value = 0
    max_indices = []  

    for i in range(5):
        lines[i] = int(lines[i])
        sum += lines[i]

        if lines[i] > max_value:
            max_value = lines[i]
            max_indices = [i]  
        elif lines[i] == max_value:
            max_indices.append(i) 

    if sum == 0:
        sum = 1

    for i in range(5):
        if i in max_indices:
            p.create_rectangle(W/5*i+5, H-80, W/5*i+80, H-80 - lines[i]/sum * 200, fill="orange")
        else:
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
    b1 = Button(o, text="Sopkovica",fg='white', command=sopkovica, bg='black', width=11, height=2)
    b1.place(x=W/5*0+5, y=H-40)

    b2 = Button(o, text="Rum", command=rum, bg='#8C4103', width=10, height=2)
    b2.place(x=W/5*1+5, y=H-40)

    b3 = Button(o, text="Punč", command=punc, bg='dark red', width=10, height=2)
    b3.place(x=W/5*2+5, y=H-40)

    b4 = Button(o, text="Medová 14°", command=medova, bg='yellow', width=10, height=2)
    b4.place(x=W/5*3+5, y=H-40)

    b5 = Button(o, text="Červené vínko", command=cervene_vinko, bg='red', width=10, height=2)
    b5.place(x=W/5*4+5, y=H-40)

def menu():
    date()
    text()
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