from tkinter import *
from PIL import ImageTk, Image 
root=Tk()
root.title("bora aprender")
root.iconbitmap("/Users/namorado/Downloads/icone.ico")

my_img = ImageTk.PhotoImage(Image.open("/Users/namorado/Downloads/ferias.png"))
mylabel = Label(image=my_img)
mylabel.pack()


button_quit=Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()