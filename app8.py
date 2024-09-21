
from tkinter import *

# Aula 011 - Python tkinter - DEFINIR LAGURA DE UM LABEL E IMPLICAÇÕES

menu_inicial =  Tk()
menu_inicial.title("Título")

Label_1 = Label(menu_inicial,
               text="Este é o label 1",
               font="Arial 20",
               bg="red",
               width=20)
Label_1.pack()

Label_2 = Label(menu_inicial,
               text="Este é o label 2",
               font="Arial 40",
               bg="red",
               width=20)
Label_2.pack()

menu_inicial.mainloop()