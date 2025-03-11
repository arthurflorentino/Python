import random

# Criando um vetor de 20 números aleatórios entre 0 e 99
vetor = [random.randint(0, 99) for _ in range(20)]

# Mostrando os números gerados
print("Números gerados:", vetor)

# Ordenando o vetor em ordem crescente
vetor.sort()

# Mostrando o vetor ordenado
print("Números ordenados:", vetor)