from tkinter import *

root = Tk()
#widht para tamaho, bg para cor do fundo
e=Entry(root, width=50,bg="white",fg="black",borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name: ")

def myClick():
    myLabel=Label(root, text="Olá " + e.get())
    myLabel.pack()
    

myButton=Button(root, text="Digite seu nome ", state=NORMAL, padx=50, pady=50,fg="blue",command=myClick)
    

myButton.pack()

root.mainloop()
