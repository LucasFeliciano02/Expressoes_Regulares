"""
WIDGETS TKINTER  =  O Tkinter fornece vários controles, como botões, etiquetas e caixas de texto usadas em um aplicativo GUI
Esses controles sao comumentes chamaddos de widgets
E esses widgets tem alguns atributos, como: Dimensões, cores, fontes, âncoras, estilos de relevo, Bitmaps e Cursores, etc..


# * Tipos de font Para Label:

Courier 13 bold
Ivy 10 bold
Verdana 13
Verdana 20 bold
System 20
Time New Roman
,relief=FLAT
,relief=SOLID  =  Deixa um quadrado em volta da label

# * Ex de Entry:

relief='solid', highlightthickness=1

# * Ex de Button:

relief=RAISED, overrelief=RIDGE

relief='flat', overrelief='solid'

"""


# https://iconarchive.com/  =  baixar icones que vao do lado do nome do app == (xxx.ico)
# https://icons8.com/icons/set/password = PNG | ou https://icon-icons.com/pt/icones/busca/?filtro=money = ICO
# pip install pillow


from tkinter import *

janela = Tk()
janela.title('Janela')
# janela.geometry('325x230')  # * largura x altura | width x height
janela.config(bg='#949293')  # * cor
# janela.iconphoto(False, PhotoImage(file='logo.png'))  OU  janela.iconbitmap('cadastro_db_icon.ico')  # * imagem do app

janela.resizable(width=False, height=False)  # Bloquia a tela cheia e deixa como nao redirecionamento


# * Centralizando o arquivo


# Dimensoes da janela
largura = 325
altura = 230

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()  # sempre deve ser chamada no final
