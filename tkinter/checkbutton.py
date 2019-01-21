from tkinter import *

def seleccionado():
    cadena = ""
    if(leche.get()):
        cadena +="con leche"
    else:
        cadena ="sin leche"
    if(azucar.get()):
        cadena +="con azucar"
    else:
        cadena +="sin azucar"
    monitor.config(text=cadena)
root = Tk()

root.title("chao")
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

Label(root, text="¿Cómo quieres el cafe?").pack(anchor="w")
Checkbutton(root, text="con leche", variable=leche, onvalue=1, offvalue=0,command=seleccionado).pack()
Checkbutton(root, text="sin leche", variable=azucar, onvalue=1, offvalue=0, command=seleccionado).pack()
monitor = Label(root)
monitor.pack()
root.mainloop()