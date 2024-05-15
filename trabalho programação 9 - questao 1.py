def imprimir_conteudo_arquivo():
    nome_arquivo = input("Por favor, informe o nome do arquivo de texto: ")
    
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
    
    print("Conteúdo do arquivo {}:".format(nome_arquivo))
    print(conteudo)

# Chamando a função para imprimir o conteúdo do arquivo
imprimir_conteudo_arquivo()