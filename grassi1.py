# =========================
# PROJETO DE ACADEMIA 
# =========================

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

janela = tk.Tk()
janela.title("Sistema Academia")
janela.geometry("800x600")

# =========================
# ESTILO
# =========================
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Arial", 10, "bold"), padding=6)
style.configure("TLabel", font=("Arial", 10))

# =========================
# HEADER
# =========================
titulo = tk.Label(
    janela,
    text="🏋 Sistema de Academia",
    font=("Segoe UI", 18, "bold"),
    bg="#1E293B",
    fg="white",
    pady=10
)
titulo.pack(fill="x")

# =========================
# ABAS
# =========================
abas = ttk.Notebook(janela)

aba_alunos = tk.Frame(abas)
aba_treino = tk.Frame(abas)
aba_ficha = tk.Frame(abas)

abas.add(aba_alunos, text="Alunos")
abas.add(aba_treino, text="Treinos")
abas.add(aba_ficha, text="Fichas")

abas.pack(fill="both", expand=True)

# =========================
# DADOS
# =========================
listaAlunos = []
listaTreinos = []
listaFichas = []

# =========================
# CLASSES
# =========================
class Aluno:
    def __init__(self, cpf, nome, telefone, objetivo):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.objetivo = objetivo

class Treino:
    def __init__(self, nome, modalidade, nivel, duracao):
        self.nome = nome
        self.modalidade = modalidade
        self.nivel = nivel
        self.duracao = duracao

class Ficha:
    def __init__(self, aluno, treino, frequencia, observacao):
        self.aluno = aluno
        self.treino = treino
        self.frequencia = frequencia
        self.observacao = observacao

# =========================
# FUNÇÕES ALUNO
# =========================
def atualizar_alunos():
    tree_alunos.delete(*tree_alunos.get_children())
    combo_alunos["values"] = [a.nome for a in listaAlunos]

    for a in listaAlunos:
        tree_alunos.insert("", "end", values=(
            a.nome, a.cpf, a.telefone, a.objetivo
        ))

def cadastrar_aluno():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    tel = entry_telefone.get()
    obj = combo_objetivo.get()

    if not cpf or not nome or not tel or not obj:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    aluno = Aluno(cpf, nome, tel, obj)
    listaAlunos.append(aluno)

    atualizar_alunos()

    entry_cpf.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    combo_objetivo.set("")

    messagebox.showinfo("Sucesso", "Aluno cadastrado!")

# =========================
# FUNÇÕES TREINO
# =========================
def atualizar_treinos():
    tree_treinos.delete(*tree_treinos.get_children())
    combo_treinos["values"] = [t.nome for t in listaTreinos]

    for t in listaTreinos:
        tree_treinos.insert("", "end", values=(
            t.nome, t.modalidade, t.nivel, t.duracao
        ))

def cadastrar_treino():
    nome = entry_treino.get()
    mod = combo_modalidade.get()
    nivel = combo_nivel.get()
    dur = entry_duracao.get()

    if not nome or not mod or not nivel or not dur:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    treino = Treino(nome, mod, nivel, dur)
    listaTreinos.append(treino)

    atualizar_treinos()

    entry_treino.delete(0, tk.END)
    combo_modalidade.set("")
    combo_nivel.set("")
    entry_duracao.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Treino cadastrado!")

# =========================
# FUNÇÃO FICHA
# =========================
def gerar_ficha():
    aluno = combo_alunos.get()
    treino = combo_treinos.get()
    freq = combo_ficha.get()
    obs = entry_obs.get()

    if not aluno or not treino or not freq:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios")
        return

    ficha = Ficha(aluno, treino, freq, obs)
    listaFichas.append(ficha)

    tree_fichas.insert("", "end", values=(aluno, treino, freq, obs))

    combo_alunos.set("")
    combo_treinos.set("")
    combo_ficha.set("")
    entry_obs.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Ficha criada!")

# =========================
# ABA ALUNOS
# =========================
frame_alunos = ttk.LabelFrame(aba_alunos, text="Cadastro de Alunos", padding=10)
frame_alunos.pack(fill="x", padx=10, pady=10)

tk.Label(frame_alunos, text="CPF").grid(row=0, column=0)
entry_cpf = tk.Entry(frame_alunos)
entry_cpf.grid(row=0, column=1)

tk.Label(frame_alunos, text="Nome").grid(row=1, column=0)
entry_nome = tk.Entry(frame_alunos)
entry_nome.grid(row=1, column=1)

tk.Label(frame_alunos, text="Telefone").grid(row=2, column=0)
entry_telefone = tk.Entry(frame_alunos)
entry_telefone.grid(row=2, column=1)

tk.Label(frame_alunos, text="Objetivo").grid(row=3, column=0)
combo_objetivo = ttk.Combobox(frame_alunos, state="readonly")
combo_objetivo["values"] = ["Ganhar Músculo", "Perder Gordura", "Manter"]
combo_objetivo.grid(row=3, column=1)

tk.Button(frame_alunos, text="Cadastrar", command=cadastrar_aluno).grid(
    row=4, column=0, columnspan=2, pady=5
)

tree_alunos = ttk.Treeview(
    aba_alunos,
    columns=("Nome", "CPF", "Telefone", "Objetivo"),
    show="headings"
)

for col in ("Nome", "CPF", "Telefone", "Objetivo"):
    tree_alunos.heading(col, text=col)
    tree_alunos.column(col, width=120)

tree_alunos.pack(fill="both", expand=True)

# =========================
# ABA TREINOS
# =========================
frame_treino = ttk.LabelFrame(aba_treino, text="Cadastro de Treinos", padding=10)
frame_treino.pack(fill="x", padx=10, pady=10)

tk.Label(frame_treino, text="Nome").grid(row=0, column=0)
entry_treino = tk.Entry(frame_treino)
entry_treino.grid(row=0, column=1)

tk.Label(frame_treino, text="Modalidade").grid(row=1, column=0)
combo_modalidade = ttk.Combobox(frame_treino, state="readonly")
combo_modalidade["values"] = ["Cardio", "Musculação", "Híbrido"]
combo_modalidade.grid(row=1, column=1)

tk.Label(frame_treino, text="Nível").grid(row=2, column=0)
combo_nivel = ttk.Combobox(frame_treino, state="readonly")
combo_nivel["values"] = ["Iniciante", "Intermediário", "Avançado"]
combo_nivel.grid(row=2, column=1)

tk.Label(frame_treino, text="Duração(Em Min)").grid(row=3, column=0)
entry_duracao = tk.Entry(frame_treino)
entry_duracao.grid(row=3, column=1)

tk.Button(frame_treino, text="Cadastrar", command=cadastrar_treino).grid(
    row=4, column=0, columnspan=2
)

tree_treinos = ttk.Treeview(
    aba_treino,
    columns=("Nome", "Modalidade", "Nível", "Duração"),
    show="headings"
)

for col in ("Nome", "Modalidade", "Nível", "Duração"):
    tree_treinos.heading(col, text=col)
    tree_treinos.column(col, width=120)

tree_treinos.pack(fill="both", expand=True)

# =========================
# ABA FICHAS
# =========================
frame_ficha = ttk.LabelFrame(aba_ficha, text="Gerar Ficha", padding=10)
frame_ficha.pack(fill="x", padx=10, pady=10)

tk.Label(frame_ficha, text="Aluno").grid(row=0, column=0)
combo_alunos = ttk.Combobox(frame_ficha, state="readonly")
combo_alunos.grid(row=0, column=1)

tk.Label(frame_ficha, text="Treino").grid(row=1, column=0)
combo_treinos = ttk.Combobox(frame_ficha, state="readonly")
combo_treinos.grid(row=1, column=1)

tk.Label(frame_ficha, text="Frequência").grid(row=2, column=0)
combo_ficha = ttk.Combobox(frame_ficha, state="readonly")
combo_ficha["values"] = ["1x", "2x", "3x", "4x", "5x", "6x"]
combo_ficha.grid(row=2, column=1)

tk.Label(frame_ficha, text="Obs").grid(row=3, column=0)
entry_obs = tk.Entry(frame_ficha)
entry_obs.grid(row=3, column=1)

tk.Button(frame_ficha, text="Gerar Ficha", command=gerar_ficha).grid(
    row=4, column=0, columnspan=2, pady=5
)
# Mostra os dados das fichas em tabela
tree_fichas = ttk.Treeview(
    aba_ficha,
    columns=("Aluno", "Treino", "Frequência", "Obs"),
    show="headings"
)

for col in ("Aluno", "Treino", "Frequência", "Obs"):
    tree_fichas.heading(col, text=col)
    tree_fichas.column(col, width=120)

tree_fichas.pack(fill="both", expand=True)

janela.mainloop()