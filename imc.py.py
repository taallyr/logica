
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc < 16:
    classificacao = "Magreza grave"
elif imc < 17:
    classificacao = "Magreza moderada"
elif imc < 18.25:
    classificacao = "Magreza leve"
elif imc < 25:
    classificacao = "Saudável"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"

print(f"IMC: {imc:.2f}")
print(f"Classificacao: {classificacao}")