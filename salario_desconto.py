# Programa para calcular descontos de INSS e IRRF

# ENTRADA
salario = float(input("Digite o salário (R$): "))

# PROCESSAMENTO
# Cálculo do INSS (exemplo simplificado)
if salario <= 1320:
    inss = salario * 0.075
elif salario <= 2571.29:
    inss = salario * 0.09
elif salario <= 3856.94:
    inss = salario * 0.12
else:
    inss = salario * 0.14

salario_base = salario - inss

# Cálculo do IRRF (exemplo simplificado)
if salario_base <= 2112:
    irrf = 0
elif salario_base <= 2826.65:
    irrf = salario_base * 0.075
elif salario_base <= 3751.05:
    irrf = salario_base * 0.15
elif salario_base <= 4664.68:
    irrf = salario_base * 0.225
else:
    irrf = salario_base * 0.275

salario_liquido = salario - inss - irrf

# SAÍDA
print(f"Salário bruto: R$ {salario:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")