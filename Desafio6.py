import random

# Função para o jogo de adivinhação com 4 tentativas
def jogo_adivinha():
    numero_sorteado = random.randint(1, 10)
    tentativas = 4
    
    print("Tente adivinhar o número sorteado entre 1 e 10.")
    
    for tentativa in range(tentativas):
        numero = int(input(f"Tentativa {tentativa + 1}: "))
        
        if numero == numero_sorteado:
            print("Você acertou!")
            break
        elif tentativa == tentativas - 1:
            print(f"Você errou! O número sorteado era {numero_sorteado}.")
        else:
            print("Tente novamente.")

# Chamando a função para jogar
jogo_adivinha()