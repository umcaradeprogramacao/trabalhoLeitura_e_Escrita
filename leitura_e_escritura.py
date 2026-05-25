""" PROGRAMA DE LEITURA E ESCRITURA DE ARQUIVOS DE TEXTO OU SEJA.TXT """
"""ISTO POR ENQUANTO É UM RASCUNHO, POR ISSO ESTOU UTILIZANDO NOME COMO POR EXEMPLO"""
"""  O "a" faz o arquivo ser adicionado sem apagar """
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
from datetime import datetime

def escrever_arquivo():
        texto = input("Escreva seu nome: ")

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        """O f"{..} é uma f-string ela tem função de misturar variaveis e texto dentro 
        de uma mesma string"""
        with open("nome.txt", "w") as arquivo:
                arquivo.write(f"{texto} - {data}\n")

def ler_arquivo():
    try:
            with open("nome.txt", "r") as arquivo:
                conteudo = arquivo.read()

                if conteudo == "":
                      print("Arquivo vazio!")
                else:
                      print("\n Conteudo do arquivo: ")
                      print(conteudo)
    except FileNotFoundError:
          print("Arquivo não encontrado!")
    

while True:
    print("\n===== MENU =====")
    print("1 - Escrever")
    print("2 - Ler")
    print("3 - Sair")

    opcao = input("Escolha a Opção: ")

    if opcao == "1":
        escrever_arquivo()

    elif opcao == "2":
        ler_arquivo()

    elif opcao == "3":
         print("Programa encerrado!")
         break
    else:
        print("Opção inválida!")
