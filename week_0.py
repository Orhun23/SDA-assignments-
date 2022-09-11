
#yo cozo
from tkinter import *
from turtle import bgcolor

root = Tk() 

canvas =Canvas(root, height=500, width= 500,)
canvas.create_rectangle(50,50,250,250, fill="purple")
canvas.create_polygon(150,0,150,150,0,150,fill="green")
canvas.create_arc(200,200,300,300,fill="red",extent=180,width=1)

canvas.pack()

root.mainloop()