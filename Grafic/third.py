from tkinter import *

root = Tk()
#podemos fazer tudo na mesma linha de código, mas a depender do programa e do tamanho do código, pode ser melhor realmente fazer como no second, em duas etapas (para entender veja second) (primeiro criamos depois posicionamos)
myLabel1=Label(root, text="Hello, World!").grid(row=0, column=0)
myLabel2=Label(root, text="My name is Denis").grid(row=1, column=2)
myLabel3=Label(root, text="                 ").grid(row=1, column=1)


root.mainloop()
