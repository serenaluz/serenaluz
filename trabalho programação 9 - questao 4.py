def encontrar_nome_por_numero(numero):
    nome_arquivo = "exemplo.txt"
    encontrado = False
    
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            partes = linha.split()
            if len(partes) == 2:
                nome, num = partes
                if num == numero:
                    print("O nome correspondente ao número {} é: {}".format(numero, nome))
                    encontrado = True
                    break
    
    if not encontrado:
        print("Número {} não encontrado no arquivo.".format(numero))

# Pedindo ao usuário para informar o número
numero = input("Por favor, informe um número: ")

# Chamando a função para encontrar o nome correspondente ao número informado
encontrar_nome_por_numero(numero)
