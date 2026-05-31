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
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox

class SistemaDeArquivos:
    def __init__(self):
       
        # ======
        # Janela
        # ======
        self.janela = tk.Tk()
        self.janela.title("Sistema de Arquivos")
        self.janela.geometry("500x400")
       
        # =================
        # Diretorios/Pastas
        # =================
        self.Pasta_Dados = "dados"
        self.Arquivo = "nome.txt"
       
       
        os.makedirs(self.Pasta_Dados, exist_ok=True)
       
        self.caminho = os.path.join(
            self.Pasta_Dados,
            self.Arquivo
        )
        # =================
        # Criar Componentes
        # =================
        self.criar_widgets()
        self.ler_arquivo()
       
        # ========================
        # Componentes Da Janelinha
        # ========================
    def criar_widgets(self):
       
        self.entradaNome = tk.Entry(
        self.janela,
         width=40
         )
        self.entradaNome.pack(pady=5)    
       
        self.botaoSalvar = tk.Button(self.janela,text="Salvar Dados",command=self.escrever_arquivo, width=40)
        self.botaoSalvar.pack(pady=5)

        self.botaoLer = tk.Button(
        self.janela,
        text="Ler Dados",
        command=self.ler_arquivo,
        width=40
        )
       
        self.botaoLer.pack(pady=5)

        self.caixaTexto = tk.Text(
        self.janela,
         width=50,
         height=15
         )
        self.caixaTexto.pack(pady=10)
       
        # =========
        # Main Loop
        # =========
        self.janela.mainloop() # Inicia o loop da interface gráfica, (MANTÉM A JANELA ABERTA E ESPERANDO ALGUMA INTERAÇÃO)

    def escrever_arquivo(self):
            nome = self.entradaNome.get().strip()
           
            if nome == "":
                messagebox.showwarning(
                "Aviso", "Digite um nome!"
                )
                return

            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            """O f"{..} é uma f-string ela tem função de misturar variaveis e texto dentro
            de uma mesma string"""
                   
            try:
                with open(self.caminho,
                        "a",
                        encoding="utf-8"
                        ) as arquivo:
                    arquivo.write(
                    f"{nome} - {data}\n"
                    )
                   
                messagebox.showinfo(
                     "Sucesso!",
                     "Seus Dados foram salvos!"
                )
               
                self.entradaNome.delete(0, tk.END)
                   
            except Exception as erro:
                messagebox.showerror(
                     "Erro",
                f"Erro identificado: {erro}"
                )
    # =================
    # LER # LER ARQUIVO
    # =================

    def ler_arquivo(self):
        self.caixaTexto.delete("1.0",tk.END)
        try:
                with open(self.caminho, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()

                    if conteudo == "":
                        self.caixaTexto.insert(tk.END,"Arquivo Vazio!")
                    else:
                        self.caixaTexto.insert(tk.END, conteudo)
        except FileNotFoundError:
            self.caixaTexto.insert(tk.END, "Arquivo não encontrado!")
        except PermissionError:
            self.caixaTexto.insert(
                tk.END,
                "Sem Permissão!"
            )