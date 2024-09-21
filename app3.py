from tkinter import *

# Aula 006 - Python tkinter - ALTERAR PROPRIEDADE E ADICIONAR UM BOTÃO

menu_inicial = Tk()
menu_inicial.title("Título")
#menu_inicial['bg'] = "blue"
menu_inicial.geometry("400x300")

# botão
btn = Button(menu_inicial, text= "Executar")
btn.pack()
menu_inicial.mainloop()