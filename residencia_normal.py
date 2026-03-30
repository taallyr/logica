# Programa para calcular a conta de água (residência normal)

# Entrada
consumo = float(input("Digite o consumo de água da residencia normal (m³): "))

# Processamento
if consumo <= 10:
    valor = 22.38  # valor fixo
elif consumo <= 20:
    valor = consumo * 3.50
elif consumo <= 50:
    valor = consumo * 8.75
else:
    valor = consumo * 9.64

# Saída
print(f"Valor da conta = R$ {valor:.2f}")