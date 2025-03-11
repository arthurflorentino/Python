import random

# Função para o jogo de JoKenPo
def jogo_jokenpo():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    computador = random.choice(opcoes)
    
    # Perguntando a escolha do jogador
    jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
    
    # Verificando quem venceu
    print(f"Computador escolheu: {computador}")
    
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'Pedra' and computador == 'Tesoura') or \
         (jogador == 'Papel' and computador == 'Pedra') or \
         (jogador == 'Tesoura' and computador == 'Papel'):
        print("Você venceu!")
    else:
        print("O computador venceu!")

# Chamando a função para jogar
jogo_jokenpo()