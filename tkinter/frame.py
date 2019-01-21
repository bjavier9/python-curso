from tkinter import *

root = Tk()
root.title("gato")
root.resizable(1,1)

frame = Frame(root,width=480,height=320)
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate")
frame.config(bg="Gray")
frame.config(bd=25)
frame.config(relief="sunken")
frame.config(cursor="arrow")
frame.config(bg="Yellow")
frame.config(bd=15)
frame.config(relief="ridge")



root.mainloop()