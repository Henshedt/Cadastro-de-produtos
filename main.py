import tkinter as tk
from tkinter import ttk
import datetime as dt


lista_tipos = ["Fralda",  "Lenço umedecido", "Talco", "Unidade"]
lista_cod = []

janela = tk.Tk()

# Funções


def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M:%S")
    codigo = len(lista_cod) + 1
    codigo_str = "COD-{}".format(codigo)
    lista_cod.append((codigo_str, descricao, tipo, quantidade, data_criacao))


# Titulo
janela.title('Cadastro de produtos')

label_descricao = tk.Label(text="Descrição do material")
label_descricao.grid(row=1, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

label_unidade = tk.Label(text="Tipo da unidade do material")
label_unidade.grid(row=3, column=0, padx=10, pady=10,
                   sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(
    row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

label_quantidade = tk.Label(text="Quantidade do tipo de unidade")
label_quantidade.grid(row=4, column=0, padx=10, pady=10,
                      sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10,
                      sticky='nswe', columnspan=2)

botao_criarcodigo = tk.Button(text="Gerar código", command=inserir_codigo)
botao_criarcodigo.grid(row=5, column=0, padx=10, pady=10,
                       sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_cod)
