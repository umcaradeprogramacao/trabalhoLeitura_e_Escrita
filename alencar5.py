"""
SISTEMA DE DIÁRIO PESSOAL

Objetivo:
Desenvolver uma aplicação desktop utilizando Python e Tkinter
capaz de realizar operações de leitura e escrita de arquivos
de texto (.txt).

Principais funcionalidades:

- Cadastro de usuários
- Login de usuários
- Criação de diários pessoais
- Leitura de registros salvos
- Edição de registros existentes
- Exclusão de registros
- Organização dos arquivos por usuário
- Registro automático de data e hora

Bibliotecas utilizadas:

- tkinter: criação da interface gráfica
- os: manipulação de arquivos e diretórios
- datetime: obtenção da data e hora atuais
- sys: exibição do interpretador Python utilizado

O projeto foi desenvolvido aplicando conceitos de:

- Programação Orientada a Objetos (POO)
- Classes e Objetos
- Métodos
- Encapsulamento
- Manipulação de Arquivos
- Tratamento de Exceções
- Interface Gráfica
"""

# datetime: utilizado para obter a data e hora atuais
from datetime import datetime
# os: permite criar pastas, verificar arquivos e manipular caminhos
import os
# tkinter: biblioteca gráfica utilizada para criar as janelas
import tkinter as tk
# messagebox: caixas de diálogo (erro, aviso e sucesso)
from tkinter import messagebox
# sys: utilizado apenas para exibir o interpretador Python utilizado
import sys
print(sys.executable)


          



class UsuarioService:
     """
    Classe responsável por gerenciar os usuários do sistema.

    Funções:
    - Cadastrar usuários
    - Verificar login
    - Verificar se um usuário já existe

    Os dados são armazenados em um arquivo texto
    chamado usuarios.txt.
    """
     def __init__(self):
          # Arquivo onde serão armazenados os usuários
          self.arquivo_usuarios = "usuarios.txt"
     def verificar_login(self,usuario, senha):
          """
          Procura o usuário dentro do arquivo usuarios.txt.

          Retorna:
          True  -> usuário e senha encontrados
          False -> usuário inexistente ou senha incorreta
          """

          if not os.path.exists(self.arquivo_usuarios):
               return False
          
          with open(
               self.arquivo_usuarios,
               "r",
               encoding="utf-8"
          ) as arquivo:
               
               for linha in arquivo:

                    linha = linha.strip()

                    if not linha:
                         continue

                    user, pwd = linha.strip().split(";")

                    if user == usuario and pwd == senha:
                         return True
          return False
     def user_duplicado(self,usuario):
         """
         Verifica se o nome de usuário informado
         já está cadastrado no sistema.

         Isso impede que dois usuários possuam
         o mesmo login.
         """  

         if not os.path.exists(self.arquivo_usuarios):
               return False

         with open(
             self.arquivo_usuarios,
               "r",
          encoding="utf-8"
     ) as arquivo:
     
          for linha in arquivo:

               linha = linha.strip()



               if not linha:
                    continue

               user, pwd = linha.split(";")

               if user == usuario:
                    return True

          return False
          
     def cadastrar_usuario(self, usuario,senha):
         """
         Salva um novo usuário no arquivo usuarios.txt.

         Formato salvo:
         usuario;senha
         """
         with open(
                    self.arquivo_usuarios,
                    "a",
                    encoding="utf-8",
               ) as arquivo:

                
                    arquivo.write(f"{usuario};{senha}\n")


class TelaLogin:
     """
    Tela inicial do sistema.

    Responsável por:
    - Realizar login
    - Cadastrar novos usuários
    - Abrir o diário após autenticação
     """

     def __init__(self): # == Construtor == É executado automaticamente quando fazemos login = telalogin 
         
         self.usuario_service = UsuarioService() # cria um objeto da classe responsavel pelos users 
         
         # Cria a janela principal de login
         self.janela = tk.Tk() # Aqui o tk.Tk() cria a janela da tela de login
         # Define o título da janela
         self.janela.title("Login") # Mostra o titulo "Login" que será exibido na tela
         # Define largura e altura da janela
         self.janela.geometry("300x200") # Aqui o .geometry define o tamamho da tela, a esquerda é a largura e a direita a altura.

         tk.Label( # Aqui o tk.Label cria um texto fixo que neste caso seria "Usuario"
              self.janela,
              text="Usuario"
         ).pack(pady=5)
         # Campo onde o usuário digita seu login
         self.entry_usuario = tk.Entry( # o tk.Entry cria a caixa ondeo  usuario pode digitar
              self.janela,
         )
         self.entry_usuario.pack() # exibe na tela a interface, sem o .pack ele não mostra nada.

         tk.Label( # Aqui o tk.Label cria um texto fixo que neste caso seria "Usuario"
              self.janela,
              text="Senha"
         ).pack(pady=5)
         # Campo de senha.
         # O parâmetro show="*" oculta os caracteres digitados.
         self.entry_senha = tk.Entry(
              self.janela,
               show="*"  # o show neste caso moostra na caixa de digitação da senha o simbolo "*"", voce digita a senha normalmente contudo, na hora de escrever a estrela e oque aparece visualmente.         
         )
         self.entry_senha.pack()
         # Ao clicar no botão será executada 
         # a função login()
         tk.Button(
              self.janela, # cria a interface do botao
              text="Entrar", # cria o texto do botao neste caso "Entrar"
              command=self.login # command significa quando clicar executar a funçao login
         ).pack(pady=5)

         tk.Button(
              self.janela,
              text="Cadastrar",
              command=self.cadastrar
         ).pack(pady=5)


     
     def login(self, pasta = "dados"):
         """
         Verifica se o usuário existe.

         Se o login estiver correto:
         - Fecha a tela de login
         - Abre a tela principal do diário

       
        Caso contrário:
        - Exibe mensagem de erro
        """

         usuario = self.entry_usuario.get() # O .get pega o user digitando
         senha = self.entry_senha.get() # Mesma coisa mas agora com a senha

          
         if self.usuario_service.verificar_login( # chama a função verificar_login
             usuario,
             senha  
          ):
               messagebox.showinfo(
                    "Sucesso",
                    "Login realizado!"
               )


               self.janela.destroy() # Fecha a tela de login

               self.pastaUser = os.path.join(
                    pasta,
                    usuario
               )

               app = Interface(usuario) # Abre o diario e sabe quem está logado
               app.executar() # Inicia o loop da janela, o loop mantém o tkinter rodando

         else:

               messagebox.showerror(
                    "Erro",
                    "Usuario ou senha inválidos"
               )

     def cadastrar(self):
          """
    Realiza o cadastro de um novo usuário.

    Etapas:
    1. Captura usuário e senha
    2. Verifica campos vazios
    3. Verifica se o usuário já existe
    4. Salva no arquivo usuarios.txt
          """
          # Captura Dados
          usuario = self.entry_usuario.get()
          senha = self.entry_senha.get()
          # Verifica campoos vazios
          if usuario == "" or senha == "":
               messagebox.showwarning(
                    "Aviso",
                    "Preencha todos os campos"
               )
               return
          # Verifica se o usuario foi duplicado
          if self.usuario_service.user_duplicado(usuario):
               messagebox.showwarning(
            "Aviso",
            "Nome de usuário já existe"
              )
               return
          # Salva o usuarion e senha 
          self.usuario_service.cadastrar_usuario(
               usuario,
               senha
          )
          # Mostra na tela do usuario, que o usuario foi cadastrado com Sucesso
          messagebox.showinfo(
               "Sucesso",
               "Usuario Cadastrado"
          )
     # Inicia a janela
     def executar(self):
          self.janela.mainloop() # mantém a janela aberta

class ArquivoService:
    def __init__(self,usuario, pasta="dados"): # Construtor (init)
    
        # =================
        # Diretorios/Pastas
        # =================
        self.pasta = os.path.join(
             pasta,
             usuario
        ) # Salva o nome da pasta  
        # Cria uma pasta exclusiva para o usuário.
        os.makedirs(self.pasta, exist_ok=True) # makedirs = "Fazer Diretorios/Pastas", cria a pasta.
       # exist_ok = 

    def salvar(self,titulo, conteudo):
        """
    Cria um arquivo .txt contendo:

    - Data de criação
    - Conteúdo digitado pelo usuário

    Exemplo:
    MinhaViagem.txt
        """
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Gera data, strftime =

        caminho = os.path.join( # Cria caminho
             self.pasta,
             f"{titulo}.txt"
        )
        
        with open(caminho, "w", encoding="utf-8") as arquivo: # Abri Arquivo, encoding = Deixa ter acento nas palavras
            arquivo.write(f"Data: {data}\n\n")

            arquivo.write(conteudo)

    def ler_arquivo(self, nome_arq):
        """
    Abre e retorna o conteúdo de um diário.

    Caso o arquivo não exista,
    retorna uma mensagem informando o erro.
         """

        caminho = os.path.join(
             self.pasta,
             nome_arq
        )

        try:
               with open(caminho, "r", encoding="utf-8") as arquivo:
                    return arquivo.read()

        except FileNotFoundError:
               return "Arquivo não encontrado"
             


class Interface:
   """
    Tela principal do Diário Pessoal.

    Funcionalidades:
    - Criar registros
    - Salvar registros
    - Abrir registros antigos
    - Editar registros
    - Excluir registros
    """

   def executar(self): # iNICIA O LOOP DA JANELA, SEM ESTAS 2 LINHAS A JANELA FECHA INSTANTANEAMENTE
        self.janela.mainloop()

   def __init__(self, usuario):
        self.usuario = usuario # Serve para lembrar qual usuario esta logado
        
        self.arquivo = ArquivoService(usuario)

        self.janela = tk.Tk() # Cria a janela principal

        self.janela.configure(bg="#2C3E50") # Configura cor de fundo
        self.janela.title("Diario Pessoal")
        self.janela.geometry("900x600")

        # ======
        # Janela
        # ======
        label_data = tk.Label( # Label = Textos fixos ex: Titulo do Diario
             self.janela,
             text=datetime.now().strftime("%d/%m/%Y"), # strftime =  
             bg="#2C3E50", # bg = 
             fg="white" # fg =
        )
        label_data.pack()

        tk.Label(
            self.janela,
            text="Titulo do Diario",
            bg="#2C3E50",
            fg="white",
            font=("Arial", 11,"bold")
            ).pack()
        tk.Label(
            self.janela,
            text="Escreva seu Registro",
            bg="#2C3E50",
            fg="white",
            ).pack()
        # Frame esquerdo:
        # utilizado para exibir a lista de arquivos
        self.frame_esq = tk.Frame(self.janela, bg="#2C3E50") # FRAME = ABAS DA JANELA, padx = espaçamento horizontal 
        self.frame_esq.pack(side="left", fill="y", padx=10)
        # Frame direito:
        # utilizado para exibir o conteúdo do diário
        self.frame_dir = tk.Frame(self.janela,bg="#2C3E50")
        self.frame_dir.pack(side="right", fill="both", expand=True)



        self.criar_widgets()
        self.atualizar_lista()

   def salvar_edicao(self):
       """
    Salva as modificações realizadas em um
    diário já existente.

    Funciona como um botão "Salvar Alterações".
       """

       if not hasattr(self, "arquivo_aberto") or self.arquivo_aberto is None:
              messagebox.showwarning( # hasattr = verifia se um objeto possui um atributo retorna true ou false, neste caso ele retorna se o objeto tem a variavel arquivo_aberto"
                   "Aviso",
                   "Nenhum arquivo aberto!"
              )
              return
         
       conteudo = self.textoDiario.get(
              "1.0",
              tk.END
         )

       caminho = os.path.join(
              self.arquivo.pasta,
              self.arquivo_aberto
         )

       with open(
            caminho,
            "w",
            encoding="utf-8"
        )     as arquivo:
        

                arquivo.write(conteudo)

                messagebox.showinfo(
                    "Sucesso",
                    "Seu Arquivo foi Atualizado!"
        )
                


    
   def criar_widgets(self):

        self.BotaoExcluir = tk.Button(
             self.janela,
             text="Excluir Diario",
             bg="#E74C3C",
             fg="white",
             command=self.excluir_diario
        )

        self.BotaoExcluir.pack(pady=5)
       
        self.entradaTitulo = tk.Entry(
        self.janela,
         width=40
         )
        self.entradaTitulo.pack(pady=5)
       
        self.botaoSalvar = tk.Button(self.janela,text="Salvar Dados",bg="#27AE60",fg="white",font=("Arial", 10, "bold"),command=self.salvar, width=40)
        self.botaoSalvar.pack(pady=5)



        self.textoDiario = tk.Text(
        self.frame_dir,
        width=60,
        height=10,
        bg="#ECF0F1", # bg = background é a cor de fundo, 
        fg="#2C3E50", # foreground ou cor da frente, é a cor do texto
        font=("Calibri",12),
        )    
            
        self.textoDiario.pack(pady=10) # PADY espaçamento vertical, ou seja um espaço de 10 pixels acima e abaixo do widget
        # Lista visual contendo todos os arquivos
        # pertencentes ao usuário logado.
        self.listaArq = tk.Listbox(
            self.frame_esq,
             width=25,
             height=15,
             bg="#34495E",
             fg="white",
             font=("Arial", 10)
        )
        self.listaArq.pack()

        self.botaoEditar = tk.Button(
             self.janela,
             text="Salvar Alterações",
             bg="#F39C12",
             fg="white",
             command=self.salvar_edicao
        )

        self.botaoEditar.pack(pady=5)


   def excluir_diario(self):
       """
    Remove permanentemente um diário.

    Antes da exclusão é exibida uma caixa
    de confirmação para evitar remoções acidentais.
       """
       selecionado = self.listaArq.curselection() # curselection = Retorna os indices selecionados ex: "diario1.txt"

       if not selecionado:
            messagebox.showwarning(
                "Aviso",
                  "Selecione um Arquivo"
             )
            return

       nome_arq = self.listaArq.get( 
             selecionado[0]
        )

       caminho = os.path.join( # Monta o endereço do arquivo chamado nome_arq dentro da pasta dados.
             self.arquivo.pasta,
             nome_arq
        )
       resposta = messagebox.askyesno( # askyesno = Ele mostra na tela uma especie de caixa de Confirmação 
             "Confirmar",
             f"Deseja Excluir {nome_arq}?"
        )

       if resposta:
            os.remove(caminho)
            self.arquivo_aberto = None # limpa a variavel
            
            self.atualizar_lista()

            self.textoDiario.delete( # Limpa campo de texto
                 "1.0", 
                 tk.END
            )

   def atualizar_lista(self):
       """
       Atualiza a lista de diários exibida
       na tela.

       Sempre que um diário é criado ou excluído,
       esta função é executada.
       """

       self.listaArq.delete(0, tk.END)

       arquivos = os.listdir(self.arquivo.pasta) # Pega os arquivos, listdir = lista todos os arquivos na pasta "dados" 

        
       for arquivo in arquivos: # percorre a lista 
          self.listaArq.insert( # Insere na lista
                  tk.END,
                  arquivo
             )
          self.listaArq.pack()

       self.listaArq.bind( # bind = Conecta um evento a uma função, significaria, quando selecionar um item da lista execute abrir_diario() 
           "<<ListboxSelect>>", # Executa ao clicar em um arquivo
       self.abrir_diario
        )

        

   def salvar(self):
        titulo = self.entradaTitulo.get().strip() # get = pega um valor

        conteudo = self.textoDiario.get( # Esta linha significa pegar o texto da caixa textoDiario começando na sua posição "1.0" ate o final tk.END.
             "1.0", # Posição
             tk.END # Final do texto
        )

        if titulo == "":
                messagebox.showwarning(
                "Aviso", "Digite um nome!"
                )
                return
        
        messagebox.showinfo(
             "Sucesso",
             "Seu Diario foi Salvo"
        )
        
        self.arquivo.salvar(
             titulo,
             conteudo
        )

        self.textoDiario.delete(
             "1.0",
             tk.END
        )

        self.entradaTitulo.delete(0,tk.END)

        self.atualizar_lista()

   def abrir_diario(self, _event): # evemt é um objeto que guarda info sobre o evento ocorrido, contudo o event não e usado, mas pelo tkinter exigir o event ele esta como parametro.
       """
    Executado quando o usuário seleciona
    um arquivo na lista.

    O conteúdo do arquivo é carregado
    para a área de texto.
       """

       selecionado = self.listaArq.curselection() # Descobre item selecionado

       if not selecionado:
            return

       self.arquivo_aberto = self.listaArq.get( # pega o nome do arquivo selecionado no listbox neste caso a lista de arquivos
             selecionado[0]
        )   

       conteudo = self.arquivo.ler_arquivo(
            self.arquivo_aberto
       )

       self.textoDiario.delete(
            "1.0",
            tk.END
        )

       self.textoDiario.insert(
            tk.END,
            conteudo
        )



if __name__ == "__main__":
  """
    Ponto inicial da aplicação.

    Cria a tela de login e inicia o loop
    principal do Tkinter.
    """
             # Não pode ficar dentro da classe SistemaDeArquivos somente fora por conta que ela que inicia o programa.
  login = TelaLogin() # Cria um objeto da classe TelaLogin
  login.executar() 


          
  

