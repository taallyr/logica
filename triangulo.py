# Programa para verificar e classificar um triângulo

# ENTRADA
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# PROCESSAMENTO
if a + b > c and a + c > b and b + c > a:
    
    if a == b and b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    resultado = f"Forma um triângulo do tipo: {tipo}"
else:
    resultado = "Os valores não formam um triângulo"

# SAÍDA
print(resultado)