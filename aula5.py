import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import showinfo
 #instalador mysql CMD
#pip install mysql-connector 

    
class Usuarios:
    def __init__(self,id,nome,sobrenome,cidade,estado,data_nascimento):
   
            self.id =  id                  
            self.nome = nome
            self.sobrenome = sobrenome
            self.cidade = cidade
            self.estado = estado
            self.data_nascimento = data_nascimento

def conexao():
    
    try:
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "banco_python"
        )

        print("conectado")
        return conexao
    
    except mysql.connector.Error as e: 
        print(f'Erro ao conectar ao servidor Mysql: {e}')

        
def desconectar(conexao):
        if conexao:
            conexao.close()

def selecionarUsuarios():
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USUARIOS")
        table = cursor.fetchall()
        print('\n Usuarios: ')
        for row in table:
                print("Id:", row[0], end="\n")
                print("Nome:", row[1], end="\n")
                print("sobrenome:", row[2], end="\n")
                print("cidade:", row[3], end="\n")
                print("estado:", row[4], end="\n")
                print("nascimento:", row[5], end="\n")

def inserirUsuarios(usuario):
        con = conexao()
        cursor = con.cursor()
        cursor.execute(
        f"INSERT INTO usuarios(id, nome, sobrenome, cidade, estado, data_nascimento)" 
        f"VALUES('{usuario.id}','{usuario.nome}','{usuario.sobrenome}','{usuario.cidade}','{usuario.estado}','{usuario.data_nascimento}')")
        con.commit()
        desconectar(con)
        
def CadastrarUsuario():
    
    janelaUsuarios = tk.Toplevel(app)
    janelaUsuarios.title("Cadastro de Usuários")
    selecionarUsuarios()

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

    #lblCadastroUsuarios_sexo = tk.Label(janelaUsuarios, text="Informe o sexo:", font="Times", foreground="black")
    #lblCadastroUsuarios_sexo.place(x=10, y=100)

    #entry_sexo = tk.Entry(janelaUsuarios)
    #entry_sexo.place(x=160,y=100)

    def salvarUsuario():
        def salvarUsuario():
            usuario = Usuarios(None, entryNome.get(), entrySobrenome.get(),entryCidade.get(),
            entryEstado.get(), entryDataNascimento.get())
            inserirUsuarios(usuario)

        #print("Usuario informado:", "\n O nome do(a) usuario(a) é:", entry_nome.get())
        #print("O sobrenome é:", entry_sobrenome.get())
        #print("A cidade é:", entry_cidade.get())
        #print("O estado é:", entry_estado.get())
        #print("A data de nascimento é:", entry_nascimento.get())
        #print("O sexo do usuario é:", entry_sexo.get())

    botao_cadastrar = tk.Button(janelaUsuarios,width=20, text= "Registrar usuario", command=salvarUsuario)
    botao_cadastrar.place(x=145, y= 110)

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
