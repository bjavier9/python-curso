from tkinter import *
from tkinter import messagebox as Messagebox

root = Tk()

def test():
    # Messagebox.showwarning("hola", "hola mundo")
    # Messagebox.showinfo("hola", "hola mundo")
    # Messagebox.showerror("hola", "hola mundo")
    # resultado = Messagebox.askquestion("hola", "hola estas seguro que quieres irte?")
    # if resultado =="yes":
    #     root.detroy()
    # resultado = Messagebox.askokcancel("hola", "hola estas seguro que quieres irte?")
    # resultado = Messagebox.askyesno("hola", "hola estas seguro que quieres irte?")
    # if resultado:
    #     root.destroy()
    resultado = Messagebox.askretrycancel("reintentar","no se puede conectar")
    if resultado:
        root.destroy()
Button(root, text="click", command=test).pack()

root.mainloop()