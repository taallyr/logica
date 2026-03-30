# Programa com menu de opções

# ENTRADA
print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Sair")

opcao = int(input("Digite uma opção: "))

# PROCESSAMENTO

if opcao == 1:
    resultado = "Você selecionou a opção 1"
elif opcao == 2:
    resultado = "Você selecionou a opção 2"
elif opcao == 3:
    resultado = "Você selecionou a opção 3"
elif opcao == 4:
    resultado = "Você selecionou sair"
else:
    resultado = "Opção inválida!!!"

# SAÍDA
print(resultado)
print("Fim do programa!")