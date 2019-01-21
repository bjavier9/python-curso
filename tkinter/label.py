from tkinter import *

root = Tk()
"""
texto = StringVar()
texto.set("hola jajjd")
Label(root, text="pelotudo").pack(anchor="nw")
label = Label(root, text="ey mira")
label.pack(anchor="center")
Label(root, text="JAJAJAJA").pack(anchor="se")

label.config(bg="green",fg="blue", font=("Verdana",24))
label.config(textvariable=texto)"""
imagen = PhotoImage(file="icon.gif")
Label(root, image=imagen, bd=0).pack(side="left")
root.mainloop()  