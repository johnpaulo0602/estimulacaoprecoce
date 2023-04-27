# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Criando janela
janela = Tk()
janela.title("Estimulação Precoce")
janela.geometry('1140x700')
janela.resizable(width=FALSE, height=FALSE)


nb = ttk.Notebook(janela)
nb.place(x=0, y=0, width=600, height=400)

# Aba home
abaHome = Frame(nb)
nb.add(abaHome, text="Home")

l_nome = Label(abaHome, text="Nome: *", height=1, anchor=NW,)
l_nome.place(x=4, y=10)
e_nomecurso = Entry(abaHome, width=35, justify='left', relief='solid')
e_nomecurso.place(x=7, y=40)

# Aba Cadastro
abaCadastro = Frame(nb)
nb.add(abaCadastro, text="Cadastro")

# Aba Turmas
abaTurmas = Frame(nb)
nb.add(abaTurmas, text="Turmas")




janela.mainloop()