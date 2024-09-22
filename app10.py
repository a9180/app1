from tkinter import *

# Aula 013 - Python tkinter - ALTURA DE UM LABEL E ALINHAMENTO DE TEXTO

menu_inicial =  Tk()
menu_inicial.title('Título')
menu_inicial.geometry("500x300")

Label_1 = Label(
    menu_inicial,
    text="Olá, Mundo!",
    font="Arial 30",
    bd=3,
    relief="solid",
    width=20,
    height=4,
    anchor=NW
).pack()

menu_inicial.mainloop()