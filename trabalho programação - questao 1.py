# -*- coding: utf-8 -*-
def criar_lista_compras():
    # Pedindo ao usuário para digitar os itens da lista de compras
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Separando os itens da entrada do usuário e armazenando-os em uma lista
    lista_compras = itens.split(',')

    # Imprimindo os itens em linhas separadas usando um loop
    print("Itens da lista de compras:")
    for item in lista_compras:
        print(item.strip())  # Removendo espaços em branco extras se houver

# Exemplo de uso da função
criar_lista_compras()