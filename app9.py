from tkinter import *

# Aula 012 - Python tkinter - LABEL COM VÁRIAS LINHAS, BORDER E RELIF

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x500")

border=2

Label1 = Label(
            menu_inicial, 
            text="solid",
            font="Arial 20",
            bd=border,
            relief="solid"
).pack()

Label1 = Label(
            menu_inicial, 
            text="flat",
            font="Arial 20",
            bd=border,
            relief="flat"
).pack()

Label1 = Label(
            menu_inicial, 
            text="raised",
            font="Arial 20",
            bd=border,
            relief="raised"
).pack()

Label1 = Label(
            menu_inicial, 
            text="sunken",
            font="Arial 20",
            bd=border,
            relief="sunken"
).pack()

Label1 = Label(
            menu_inicial, 
            text="ridge",
            font="Arial 20",
            bd=border,
            relief="ridge"
).pack()

Label1 = Label(
            menu_inicial, 
            text="groove",
            font="Arial 20",
            bd=border,
            relief="groove"
).pack()

menu_inicial.mainloop()