# Programa para calcular média e conceito do aluno

# ENTRADA
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

# PROCESSAMENTO
media = (n1 + n2 + n3 + n4) / 4

# Definição do conceito
if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

# Situação
if conceito in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# SAÍDA
print(f"Notas: {n1}, {n2}, {n3}, {n4}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")