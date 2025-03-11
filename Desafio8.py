# Programa para gerar os primeiros 10 termos da sequência de Fibonacci
def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" > ")
        a, b = b, a + b
    print("FIM")

# Chamando a função
fibonacci()