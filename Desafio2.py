# Programa para verificar se três segmentos podem formar um triângulo

# Entrada dos três segmentos de reta
a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))

# Para formar um triângulo, cada lado precisa ser menor que a soma dos outros dois
# Vamos verificar essa condição
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos NÃO podem formar um triângulo.")
