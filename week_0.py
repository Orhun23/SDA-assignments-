
#yo cozo
from tkinter import *
from turtle import bgcolor, width

root = Tk() 

canvas =Canvas(root, height=500, width= 500,)
canvas.create_rectangle(50,50,250,250, fill="purple")
canvas.create_polygon(150,0,150,150,0,150,fill="green")
canvas.create_arc(200,200,300,300,fill="red",extent=180,width=5)
canvas.create_arc(200,200,300,300,extent=180,start=180,width=5)
canvas.create_oval(270,270,230,230,fill="white",width=5 )
canvas.create_rectangle(350,350,270,270, fill="red")
exitButton = Button(root, text= "Click to exit", command=root.destroy).pack()
text = Label(root, text="the written stuff that was needed")
text.place(x=270,y=190)
canvas.pack()

root.mainloop()