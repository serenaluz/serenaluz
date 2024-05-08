def pedir_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    for nome in nomes:
        print(nome)

# Chamando a função para testar
pedir_nomes()