import random

# Função para o jogo de adivinhação
def jogo_adivinha():
    numero_sorteado = random.randint(1, 5)
    tentativa = int(input("Tente adivinhar o número sorteado (entre 1 e 5): "))
    
    if tentativa == numero_sorteado:
        print("Você acertou!")
    else:
        print(f"Você errou! O número sorteado era {numero_sorteado}.")

# Chamando a função para jogar
jogo_adivinha()