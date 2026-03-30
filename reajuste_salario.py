# Programa para calcular reajuste salarial

# ENTRADA
salario = float(input("Digite o salário (R$): "))

# PROCESSAMENTO
if salario <= 1000:
    percentual = 0.20
elif salario <= 1700:
    percentual = 0.15
elif salario <= 2300:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario * percentual
novo_salario = salario + aumento

# SAÍDA
print(f"Salário digitado: R$ {salario:.2f}")
print(f"Aumento         : {percentual*100:.0f}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário    : R$ {novo_salario:.2f}")