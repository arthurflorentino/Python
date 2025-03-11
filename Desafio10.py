# Função que recebe um número e exibe a sequência de Fibonacci
def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" > ")
        a, b = b, a + b
    print("FIM")

# Solicitando ao usuário o número de termos
num_termos = int(input("Quantos termos da sequência de Fibonacci você quer exibir? "))
Fibonacci(num_termos)