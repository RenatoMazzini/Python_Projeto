import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import showinfo
#pip install mysql-connector

class Usuarios:
        def __init__(self, id, nome,sobrenome,cidade,estado,data_nascimento):
                self.id = id
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
                print(f'Erro ao conectar no Servidor MySql: {e}')

def desconectar(conexao):
        if conexao:
                conexao.close()

def selecionarUsuarios(janelaUsuarios):
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        table = cursor.fetchall()
        print('\n Usuarios: ')

        columns = ('id','nome','sobrenome','cidade','estado','data_nascimento')
        tree = ttk.Treeview(janelaUsuarios, columns=columns, show='headings')

        #define cabeçalhos
        tree.heading('id',text='#')
        tree.heading('nome',text='Nome')
        tree.heading('sobrenome', text='Sobrenome')
        tree.heading('cidade',text='Cidade')
        tree.heading('estado',text='Estado')
        tree.heading('data_nascimento',text='Data de Nascimento')
        
        def item_selected(self):
                item = tree.focus()
        tree.bind('<<TreeviewSelect>>', item_selected)
        tree.grid(row=0, column=0, sticky=tk.NSEW)

        #adicionar uma barra de rolagem
        scrollbar = ttk.Scrollbar(janelaUsuarios, orient=tk.VERTICAL,command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1,sticky='ns')

        usuarios = []
        for row in table:
              usuarios.append((f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[4]}', f'{row[5]}'))
        for user in usuarios:
               tree.insert('',tk.END,values=user) 
def inserirUsuarios(usuario):
        con = conexao()
        cursor = con.cursor()
        cursor.execute(
        f"INSERT INTO usuarios(id, nome, sobrenome, cidade, estado, data_nascimento)" 
        f"VALUES('{usuario.id}','{usuario.nome}','{usuario.sobrenome}','{usuario.cidade}','{usuario.estado}','{usuario.data_nascimento}')")
        con.commit()
        desconectar(con)

def cadastrarUsuarios():
    janelaUsuarios = tk.Toplevel(app)
    selecionarUsuarios(janelaUsuarios)
    lblNome = tk.Label(janelaUsuarios,text="Informe o seu nome: "
            ,font="Times"
            ,foreground="black")
    lblNome.place(x=100,y=250)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=230,y=250)
    
    lblSobrenome = tk.Label(janelaUsuarios,text="Informe sobrenome: "
            ,font="Times"
            ,foreground="black")
    lblSobrenome.place(x=100,y=275)
    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=230, y=275)

    lblDataNascimento = tk.Label(janelaUsuarios,text="data de nascimento:"
            ,font="Times"
            , foreground="black")
    lblDataNascimento.place(x=100, y=300)
    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=230, y=300)

    lblCidade = tk.Label(janelaUsuarios,text="Informe a sua cidade:"
            ,font="Times"
            , foreground="black")
    lblCidade.place(x=100,y=325)
    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place(x=230,y=325)

    lblEstado = tk.Label(janelaUsuarios, text="Informe o estado: "
            ,font="Times"
            ,foreground="black")
    lblEstado.place(x=100, y=350)
    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place(x=230, y=350)
    
    def salvarUsuario():
        usuario = Usuarios(None, entryNome.get(), entrySobrenome.get(),entryCidade.get(),
        entryEstado.get(), entryDataNascimento.get())
        inserirUsuarios(usuario)
    btnSalvar = tk.Button(janelaUsuarios,width=20
            ,text="Salvar", command=salvarUsuario)
    btnSalvar.place(x=150,y=380)
    
    #entryNome.insert("end","teste")
    #entryNome.insert("end","tormes")
    
    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")
def cadastrarProdutos():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários"
            ,command=cadastrarUsuarios)
fileMenu.add_command(label="Cadastrar Produtos"
            ,command=cadastrarProdutos)
menuPrincipal.add_cascade(label="Funcao"
                        ,menu=fileMenu)


app.title("Sistema Tarumã")
app.geometry("800x600")

app.mainloop()
#app.destroy()