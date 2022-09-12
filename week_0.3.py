from cgitb import text
from posixpath import split
from shutil import move
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tokenize import String

country =[]

def displaycapital(country, con):
    found = False
    pos = 0
    while pos < len[country] and not found:
        if country[pos][0] == con:
            found = True
        pos+=1
    if found:
        return country[pos-1][1]
    else:
        messagebox.showerror(message="invalid input try some else")  

def clickArea():
    cap.set(displaycapital(country,con.get()))

def create_list():
    capitalfile = open ("data_capital_city.txt", 'r')
    for line in capitalfile:
        land = line.split()
        land.append(land)
    capitalfile.close()
    return country    

root = Tk() 

root.title("read from text file/list GUI")

Label(root,text="country").grid(row=0,column=0)
con= StringVar
Entry(root, textvariable=con).grid(row=0,column=1)
con = StringVar()
Label(root,text="capital").grid(row=2, column=0)
cap=IntVar()
Label(root,textvariable=cap).grid(row=2,column=1)

button = Button(root,text="capital is", comman=clickArea)
button.grid(row=3,column=0,columnspan=2)

create_list()
print(country)



root.mainloop()