from tkinter import *
def sumar():
    r.set(float(n1.get())+float(n2.get()))
    borrar()
def restar():
    r.set(float(n1.get())-float(n2.get()))
    borrar()
def multi():
    r.set(float(n1.get())-float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
n1=StringVar()
n2=StringVar()
r=StringVar()
Label(root, text="numero 1").pack()
Entry(root, justify="center",textvariable=n1).pack()
Label(root, text="numero 2").pack()
Entry(root, justify="center",textvariable=n2).pack()
Label(root, text="\nresultado").pack()
Entry(root, justify="center",textvariable=r, state="disabled").pack()
Button(root, text="sumar", command=sumar).pack(side="left")
Button(root, text="resta", command=restar).pack(side="left")
Button(root, text="multiplicar", command=multi).pack(side="left")

root.mainloop()