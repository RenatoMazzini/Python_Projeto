from tkinter import *
janela = Tk()
janela["bg"] = "white"
app = Frame(janela)
app.grid()

def escrever():
    print("O nome do usuario é:",entry_nome.get(),
        "\n A idade do usuario é:", entry_idade.get())

labelMsg_nome = Label(janela, text="Informe o seu nome:", font="Times", bg="white", foreground="black")
labelMsg_nome.place(x=100, y=50)

entry_nome = Entry(janela)
entry_nome.place(x=230,y=55)
 
labelMsg_idade = Label(janela, text="Informe o sua idade:", font="Times", bg="white", foreground="black")
labelMsg_idade.place(x=100, y=85)

entry_idade = Entry(janela)
entry_idade.place(x=230,y=85)

btnFalarNome = Button(janela, width=20, text="Entrar", command=escrever)
btnFalarNome.place(x=150, y=110)

tittle = "Sistema Tarumã"
janela.title(tittle)
janela.geometry("400x500")
janela.resizable(True,True)
janela.mainloop()
janela.destroy()