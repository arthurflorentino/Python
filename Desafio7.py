# Programa para calcular os 10 primeiros termos de uma PA
def pa():
    primeiro_termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))
    
    # Calculando os 10 primeiros termos da PA e a soma
    soma = 0
    for i in range(10):
        termo = primeiro_termo + i * razao
        soma += termo
        print(termo, end=' > ')
    
    print(f"\nSoma dos termos: {soma}")

# Chamando a função
pa()