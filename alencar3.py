""" PROGRAMA DE LEITURA E ESCRITURA DE ARQUIVOS DE TEXTO OU SEJA.TXT """
"""ISTO POR ENQUANTO É UM RASCUNHO, POR ISSO ESTOU UTILIZANDO NOME COMO POR EXEMPLO"""
""" O "a" faz o arquivo ser adicionado sem apagar """
""" O "w" faz escrever, mas apaga o conteudo anterior """
""" O with faz o arquivo fechar automaticamente, enquanto sem ele temos que usar
o "close()" """
""" Uso de try ( Tratamento de erros ), para evitar que o codigo quebre"""
""" Utilizamos funções para organizar melhor o codigo"""
"""Utilizamos o tratamento de excessoes somente na Leitura de arquivos por conta
que os principais erros acontecem na leitura de arquivos, já que se não iria dar o erro "FileNotFoundError" """
"""A biblioteca Datetime foi utilizada visando maior organização e para dar maior estilo ao codigo
"""
"""Na Biblioteca Datetime, usamos a função strftime() onde ela transforma a data atua vinda de
datetime.now() em formato de texto.

Neste caso o formato usado é "%d/%m/%Y %H:%M:%S" onde
%d e o dia, %m o mes, %Y o ano, %H a hora, %M o minuto e por fim %S os segundos"""
"""" A biblioteca os interage com o sistema operacional, com a funcao os.makedirs() criando diretorios
se houver já uma pasta com o mesmo nome, gera um erro FileExistsError, por isso eu uso os.makedirs(..., exist_ok=True),
caso ja exista o diretorio ele ignora, se não cria.
"""
""" A função os.path.join() junta caminhos/pastas corretamente"""
""" .strip() remove espaços vazios no começo e final da string"""
""" Nos chamamos de métodos os "def's que são funções dentro de classes"""
"""O Tkinter executa funções de botão sem argumentos."""
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox
import sys
print(sys.executable)

class ArquivoService:

    def __init__(self, pasta="dados"): # Construtor (init)
    
        # =================
        # Diretorios/Pastas
        # =================
        self.pasta = pasta # Salva o nome da pasta

        os.makedirs(self.pasta, exist_ok=True) # makedirs = "Fazer Diretorios/Pasras", cria a pasta.
       # exist_ok = 

    def salvar(self,titulo, conteudo):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Gera data, strftime =

        caminho = os.path.join( # Cria caminho
             self.pasta,
             f"{titulo}.txt"
        )
        
        with open(caminho, "w", encoding="utf-8") as arquivo: # Abri Arquivo, encoding = Deixa ter acento nas palavras
            arquivo.write(f"Data: {data}\n\n")

            arquivo.write(conteudo)

    def ler_arquivo(self, nome_arq):
        self.caminho = os.path.join(
             self.pasta,
             nome_arq
        )

        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                return arquivo.read()
        except FileNotFoundError:
             return "Arquivo vazio"
        
        self.arquivo_aberto = None

class Interface:

        

    def executar(self): # iNICIA O LOOP DA JANELA, SEM ESTAS 2 LINHAS A JANELA FECHA INSTANTANEAMENTE
        self.janela.mainloop()

    def __init__(self):

        self.janela = tk.Tk() # Cria a janela principal

        self.janela.configure(bg="#2C3E50") # Configura cor de fundo
        self.janela.title("Diario Pessoal")
        self.janela.geometry("900x600")

        self.arquivo = ArquivoService()

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

        self.frame_esq = tk.Frame(self.janela, bg="#2C3E50") # FRAME = ABAS DA JANELA, padx = 
        self.frame_esq.pack(side="left", fill="y", padx=10)

        self.frame_dir = tk.Frame(self.janela,bg="#2C3E50")
        self.frame_dir.pack(side="right", fill="both", expand=True)



        self.criar_widgets()
        self.atualizar_lista()

    def salvar_edicao(self):

         if self.arquivo_aberto is None:
              messagebox.showwarning(
                   "Aviso",
                   "Nenhum arquivo aberto!"
              )
              return
         
         if not hasattr(self, "arquivo_aberto"): # hasattr =
              return
         
         conteudo = self.textoDiario.get(
              "1.0",
              tk.END
         )

         caminho = os.path.join(
              "dados",
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

        self.botaoLer = tk.Button(
        self.janela,
        text="Ler Dados",
        bg="#3498DB",
        fg="white",
        font=("Arial", 10, "bold"),
        command=self.atualizar_texto,
        width=40
        )
       
        self.botaoLer.pack(pady=5)

        scroll = tk.Scrollbar(self.janela)
        scroll.pack(side="right", fill="y") 


        self.textoDiario = tk.Text(
        self.frame_dir,
        width=60,
        height=10,
        bg="#ECF0F1",
        fg="#2C3E50",
        font=("Calibri",12),
        yscrollcommand=scroll.set,
        )    
        scroll.config(
             command=self.textoDiario.yview
        )
        self.textoDiario.pack(pady=10)

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
        selecionado = self.listaArq.curselection() # curselection = Retorna os indices selecionados ex: "diario1.txt"

        if not selecionado:
            messagebox.showwarning(
                "Aviso",
                  "Selecione um Arquivo"
             )
            return

        nome_arq = self.listaArq.get( # get = 
             selecionado[0]
        )

        caminho = os.path.join(
             "dados",
             nome_arq
        )
        resposta = messagebox.askyesno( # askyesno = Ele mostra na tela Confirmar, Deseja Excluir S OU N
             "Confirmar",
             f"Deseja Excluir {nome_arq}?"
        )

        if resposta:
            os.remove(caminho)
            
            self.atualizar_lista()

            self.textoDiario.delete( # Limpa campo de texto
                 "1.0", 
                 tk.END
            )

    def atualizar_lista(self):

        self.listaArq.delete(0, tk.END)

        arquivos = os.listdir("dados") # Pega os arquivos 

        for arquivo in arquivos:
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
             "2.0", # Posição
             tk.END
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
            # ============
            # Atuliazar texto
            # ============
    def atualizar_texto(self):
            self.textoDiario.delete("1.0",tk.END) # Limpar texto do usuario
            conteudo = self.arquivo.ler_arquivo()
            self.textoDiario.insert(tk.END, conteudo
            )

    def abrir_diario(self, event):

        selecionado = self.listaArq.curselection() # Descobre item selecionado

        if not selecionado:
            return

        nome_arquivo = self.listaArq.get( # Obtém nome
        )   

        caminho = os.path.join( # Lê CONTEUDO
            "dados", 
            nome_arquivo
        )

        with open(
            caminho,
            "r",
            encoding="utf-8"
        ) as arquivo:

            conteudo = arquivo.read()

        self.textoDiario.delete(
            "1.0",
            tk.END
        )

        self.textoDiario.insert(
            tk.END,
            conteudo
        )

        self.arquivo_aberto = nome_arquivo


if __name__ == "__main__": # Não pode ficar dentro da classe SistemaDeArquivos somente fora por conta que ela que inicia o programa.
            app = Interface() 
            app.executar() 


          
  

