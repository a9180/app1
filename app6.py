
from tkinter import*

# Aula - 009 Python tkinter - LABEL WIDGET E COMO FUNCIONA P PACK

menu_inicial = Tk()
menu_inicial.title("Título")

Label_1 = Label(menu_inicial, text="Este é o label 1.")
Label_1.pack()
Label_2 = Label(menu_inicial, text="Este é o label 2.")
Label_2.pack()
cmd = Button(menu_inicial, text="Executar")

# pack
Label_1.pack()
Label_2.pack()
cmd.pack()

menu_inicial.mainloop()