# Programa para verificar e classificar o tipo de triângulo

# Entrada dos três segmentos de reta
a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))

# Primeiro, verificamos se os segmentos podem formar um triângulo
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos podem formar um triângulo.")

    # Agora classificamos o tipo de triângulo com base nos lados
    if a == b == c:
        print("Tipo: Triângulo Equilátero (todos os lados iguais).")
    elif a == b or a == c or b == c:
        print("Tipo: Triângulo Isósceles (dois lados iguais).")
    else:
        print("Tipo: Triângulo Escaleno (todos os lados diferentes).")
else:
    print("Os segmentos NÃO podem formar um triângulo.")
