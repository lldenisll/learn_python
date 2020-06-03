from tkinter import *
import random

root = Tk()
root.title("Jogo do Nim")


def partida():
    top=Toplevel()
    top.title("Partida")
    p1l=Label(top, text="Digite o nome do player1").grid(row=1, column=0)
    p1=Entry(top).grid(row=1, column=1)
    
    p2l=Label(top, text="Digite o nome do player2").grid(row=2, column=0)
    p2=Entry(top).grid(row=2, column=1)
    
    nl=Label(top, text="Quantas peçar os jogadores querem utilizar?").grid(row=4, column=0)
    n=Entry(top).grid(row=4, column=1)
    
    ml=Label(top, text="Qual o limite de peçar por jogada?").grid(row=5, column=0)
    m=Entry(top).grid(row=5, column=1)
    
    botaoiniciar= Button(top, text="Confirmar e iniciar partida").grid(row=6, column=1)
    
inicio=Label(root, text="Vamos começar")
inicio.grid(row=0, column=0)

botaopartida =Button(root, text="Escolha uma partida isolada", command=partida)

botaocampeonato =Button(root, text="Escolha um Campeonato") 
botaocampeonato.grid(row=1, column=0)
botaopartida.grid(row=1, column=1)

    
    






    




root.mainloop()
