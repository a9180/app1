from tkinter import *

# Aula 008 - Python tkinter - CENTRAR O FORMULÁRIO NO SCREEN  

menu_inicial = Tk()
menu_inicial.title("Título")

# dimensões da janela
largura = 500
altura = 300

# reslução do nosso sistema
largura_screen = menu_inicial.winfo_screenmmwidth()
altura_screen = menu_inicial.winfo_screenmmheight()

# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

print(largura_screen, altura_screen)

menu_inicial.mainloop()