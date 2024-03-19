# Variáveis para armazenar os dados
numero1 = 10
numero2 = 20
numero3 = 30
numero4 = 40
frase = "A luz é sempre o caminho"
palavra = "luz"

# Cálculo da média aritmética
media = (numero1 + numero2 + numero3 + numero4) / 4

# Cálculo do quadrado de um número
quadrado_numero = numero2 ** 2

# Cálculo do dobro de um número
dobro_numero = 2 * numero3

# Contagem de letras na palavra
quantidade_letras = len(palavra)

# Contagem de espaços em branco na frase
quantidade_espacos = frase.count(" ")

# Verificação se o primeiro número é maior que o segundo
primeiro_maior = numero1 > numero2

# Encontrar o maior número
maior_numero = max(numero1, numero2, numero3, numero4)

# Impressão dos resultados
print(f"Média aritmética: {media:.2f}")
print(f"Quadrado do número {numero2}: {quadrado_numero}")
print(f"Dobro do número {numero3}: {dobro_numero}")
print(f"Quantidade de letras na palavra '{palavra}': {quantidade_letras}")
print(f"Quantidade de espaços em branco na frase: {quantidade_espacos}")
print(f"O primeiro número ({numero1}) é maior que o segundo ({numero2}): {primeiro_maior}")
print(f"O maior número é: {maior_numero}")
