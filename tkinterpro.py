from tkinter import *
import tkinter
top=tkinter.Tk()
c=tkinter.Canvas(top,bg="green",height=700,width="500")
c.create_line(300,100,200,100,fill="yellow")
c.create_oval(30,40,200,250,fill="red")
c.pack()
top.mainloop()