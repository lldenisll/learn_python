from tkinter import *

root = Tk()
root.title("Nim")

e=Entry(root)
e.grid(row=0,column=0)

def button_escolha():
    if e.get() == str("Partida"):
        escolha = Toplevel()
        root.title("Partida")
        mensagem=Label(root, text="Você escolheu partida")
        mensagem.grid(row=1, column=0)
        
button_escolha=Button(root,text="Escolha", padx=79, pady=20, command=button_escolha)


button_escolha.grid(row=2, column=0)


root.mainloop()
  