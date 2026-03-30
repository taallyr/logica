# Programa para calcular a conta de água (comércio/indústria)

# Entrada
consumo = float(input("Digite o consumo de água do comercio industrial (m³): "))

# Processamento
if consumo <= 10:
    valor = 44.95  # valor fixo
elif consumo <= 20:
    valor = consumo * 8.75
elif consumo <= 50:
    valor = consumo * 16.76
else:
    valor = consumo * 17.46

# Saída
print(f"Valor da conta: R$ {valor:.2f}")