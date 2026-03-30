# Programa de calculadora com menu

# ENTRADA
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada")
print("7 - Número par")
print("8 - Número ímpar")

opcao = int(input("Escolha uma opção: "))

# PROCESSAMENTO

if opcao == 1:
    resultado = num1 + num2

elif opcao == 2:
    resultado = num1 - num2

elif opcao == 3:
    resultado = num1 * num2

elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"

elif opcao == 5:
    resultado = num1 ** num2

elif opcao == 6:
    if num1 >= 0:
        resultado = num1 ** 0.5
    else:
        resultado = "Erro: número negativo"

elif opcao == 7:
    if num1 % 2 == 0:
        resultado = "Número par"
    else:
        resultado = "Número ímpar"

elif opcao == 8:
    if num1 % 2 != 0:
        resultado = "Número ímpar"
    else:
        resultado = "Número par"

else:
    resultado = "Opção inválida"

# SAÍDA
print("Resultado:", resultado)
print("Fim do programa!")