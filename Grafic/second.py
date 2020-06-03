from tkinter import *

root = Tk()
# criando label widget definir (define)
myLabel1=Label(root, text="Hello, World!")
myLabel2=Label(root, text="My name is Denis")
#um jeito de aumentar o espaço entre as colunas
myLabel3=Label(root, text="                 ")
#nao estamos mais usando o pack, estamos usando GRID, ou seja vamos enviar o label para uma posição específica, em linhas e colunas

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)

root.mainloop()
