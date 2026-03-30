# Programa para identificar o turno de estudo

# ENTRADA
turno = input("Digite o turno (M - Matutino / V - Vespertino / N - Noturno): ")

# PROCESSAMENTO
if turno == "M":
    mensagem = "Bom Dia!"
elif turno == "V":
    mensagem = "Boa Tarde!"
elif turno == "N":
    mensagem = "Boa Noite!"
else:
    mensagem = "Valor Inválido!"

# SAÍDA
print(mensagem)