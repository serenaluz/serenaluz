def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: divisão por zero.")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida.")
                continue

            print("Resultado:", resultado)
            break

        except ValueError:
            print("Por favor, insira números válidos.")

# Chamando a função para testar
calcular()

