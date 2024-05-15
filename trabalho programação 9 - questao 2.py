def copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino):
    with open(nome_arquivo_origem, "r") as arquivo_origem:
        conteudo = arquivo_origem.read()
    
    with open(nome_arquivo_destino, "w") as arquivo_destino:
        arquivo_destino.write(conteudo)
    
    print("Conteúdo do arquivo {} copiado para o arquivo {} com sucesso.".format(nome_arquivo_origem, nome_arquivo_destino))

# Chamando a função para copiar o conteúdo do arquivo serena.txt para copia_serena.txt
copiar_conteudo_arquivo("serena.txt", "copia_serena.txt")
