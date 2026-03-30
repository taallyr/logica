# Programa para calcular o valor da conta de água
# baseado no consumo em m³

# Entrada
consumo = float(input("Digite o consumo de água da residência social (m³): "))

# Processamento
if consumo <= 10:
    valor = 7.59  # valor fixo
elif consumo <= 20:
    valor = consumo * 1.31
elif consumo <= 30:
    valor = consumo * 4.64
elif consumo <= 50:
    valor = consumo * 6.62
else:
    valor = consumo * 7.31

# Saída
print(f"Valor da conta = R$ {valor:.2f}")