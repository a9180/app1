from tkinter import *

# Aula 010 - Python tkinter - ALTERAR CORES E TIPO DE LETRA

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x300")

Label_1 = Label(menu_inicial, 
                text="Este é o label 1",
                 font="Arial")
Label_1.pack()

Label_2 = Label(menu_inicial, 
                text="Este é o label 2",
                 font="Arial 20 bold italic")
Label_2.pack()

Label_3 = Label(menu_inicial, 
                text="Este é o label 3",
                 font="Verdana 42 bold",
                 fg="#aaaaaa")
Label_3.pack()

menu_inicial.mainloop()  