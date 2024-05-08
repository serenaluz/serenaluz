def celsius_para_fahrenheit():
    while True:
        try:
            celsius = float(input("Digite a temperatura em graus Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Temperatura em Fahrenheit:", fahrenheit)
            break
        except ValueError:
            print("Por favor, insira uma temperatura válida.")

# Chamando a função para testar
celsius_para_fahrenheit()