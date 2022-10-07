from gettext import install
import tkinter as tk
import mysql.connector
 #instalador mysql CMD
#pip install mysql-connector 

def conexao():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
        db = "usuarios"
)

    print(conexao)


def CadastrarUsuario():
    
    janelaUsuarios = tk.Toplevel(app)
    janelaUsuarios.title("Cadastro de Usuários")

    lblCadastroUsuarios_nome = tk.Label(janelaUsuarios, text="Informe o nome:", font="Times", foreground="black")
    lblCadastroUsuarios_nome.place(x=10, y=0)    

    entry_nome = tk.Entry(janelaUsuarios)
    entry_nome.place(x=160,y=0)

    lblCadastroUsuarios_sobrenome = tk.Label(janelaUsuarios, text="Informe o sobrenome:", font="Times", foreground="black")
    lblCadastroUsuarios_sobrenome.place(x=10, y=20)

    entry_sobrenome = tk.Entry(janelaUsuarios)
    entry_sobrenome.place(x=160,y=20)

    lblCadastroUsuarios_nascimento = tk.Label(janelaUsuarios, text="Data de nascimento:", font="Times", foreground="black")
    lblCadastroUsuarios_nascimento.place(x=10, y=40)    

    entry_nascimento = tk.Entry(janelaUsuarios)
    entry_nascimento.place(x=160,y=40)

    lblCadastroUsuarios_cidade = tk.Label(janelaUsuarios, text="Informe a cidade:", font="Times", foreground="black")
    lblCadastroUsuarios_cidade.place(x=10, y=60)

    entry_cidade = tk.Entry(janelaUsuarios)
    entry_cidade.place(x=160,y=60)

    lblCadastroUsuarios_estado = tk.Label(janelaUsuarios, text="Informe o estado:", font="Times", foreground="black")
    lblCadastroUsuarios_estado.place(x=10, y=80)
    
    entry_estado = tk.Entry(janelaUsuarios)
    entry_estado.place(x=160,y=80)

    lblCadastroUsuarios_sexo = tk.Label(janelaUsuarios, text="Informe o sexo:", font="Times", foreground="black")
    lblCadastroUsuarios_sexo.place(x=10, y=100)

    entry_sexo = tk.Entry(janelaUsuarios)
    entry_sexo.place(x=160,y=100)

    def registrar_usuario():
        print("Usuario registrado", "\n O nome do(a) usuario(a) é:", entry_nome.get())
        print("O sobrenome é:", entry_sobrenome.get())
        print("A data de nascimento é:", entry_nascimento.get())
        print("A cidade é:", entry_cidade.get())
        print("O estado é:", entry_estado.get())
        print("O sexo do usuario é:", entry_sexo.get())

    botao_cadastrar = tk.Button(janelaUsuarios,width=20, text= "Registrar usuario", command=registrar_usuario)
    botao_cadastrar.place(x=145, y= 130)

    janelaUsuarios.geometry("800x600")

def CadastrarProdutos():
    janelaProdutos = tk.Toplevel(app)
    janelaProdutos.title("Cadastro de Produtos")
    janelaProdutos.geometry("800x600")
    
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários",
                             command=CadastrarUsuario) 
    
fileMenu.add_command(label="Cadastrar Produtos",
                    command=CadastrarProdutos)                            

menuPrincipal.add_cascade(label="Função", menu=fileMenu)

#buttonExample = tk.Button(app,
               # text="entrar",
               #command=Login)
#buttonExample.place(x=10, y=10)

app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()   
app.destroy()
