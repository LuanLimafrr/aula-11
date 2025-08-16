# print('Lista de alunos senacrio :\n')

# nomes = []

# for i in range(3):
#     nome = input(f'Digite o nome do {i+1}º Aluno: ')
#     nomes.append(nome)

# def saudaçao ():
#     print(f'Olá {nomes}, sejam bem vindos à turma de python 2025!')


# saudaçao ()


import tkinter as tk
from tkinter import messagebox

# Funções matemáticas
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

# Função que lida com a operação
def calcular(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if op == '+':
            resultado = soma(a, b)
        elif op == '-':
            resultado = sub(a, b)
        elif op == '*':
            resultado = multi(a, b)
        elif op == '/':
            resultado = div(a, b)
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora em Python")
janela.geometry("300x250")

# Entrada de dados
tk.Label(janela, text="Primeiro número:").pack()
entry1 = tk.Entry(janela)
entry1.pack()

tk.Label(janela, text="Segundo número:").pack()
entry2 = tk.Entry(janela)
entry2.pack()

# Botões de operação
tk.Label(janela, text="Escolha a operação:").pack(pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

tk.Button(frame_botoes, text="+", width=5, command=lambda: calcular('+')).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", width=5, command=lambda: calcular('-')).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="*", width=5, command=lambda: calcular('*')).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="/", width=5, command=lambda: calcular('/')).grid(row=0, column=3, padx=5)

# Resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=20)

# Iniciar a janela
janela.mainloop()
