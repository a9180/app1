from tkinter import *

# Aula 007 - Python tkinter - ASSOCIAR EVENTO A UM BOTÃO

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("400x300")

def cmd_Click(mesagem):
    print(mesagem)

#botão
cmd = Button(menu_inicial, text="Executar", command=lambda: cmd_Click("Olá, Novo Mundo!"))
cmd.pack()

cmd = Button(menu_inicial, text="Clicar", command=lambda: cmd_Click("Bem-vindo(a) ao marvilhoso mundo do python"))
cmd.pack()

menu_inicial.mainloop()