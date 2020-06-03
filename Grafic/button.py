from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root, text="Eu cliquei")
    myLabel.pack()
#definindo o botão, o texto que aparece e o estado, podemos aplcicar o estado DISABLED nesse caso o botão não poderá ser clicado
#padx e pady = tamanho do botão (horizontal e vertical)
#em Python sempre usamos parenteses em comandos, no caso do botão (comand), não usamos
# para dar cores as letras usamos o fg, e para o fundo bg como no ex a baixo
myButton=Button(root, text="Olha um botao!", state=NORMAL, padx=50, pady=50, bg= "#856ff8",fg="blue",command=myClick)
    

myButton.pack()

root.mainloop()
