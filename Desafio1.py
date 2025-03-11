# Programa para calcular a redução do tempo de vida de um fumante

# Perguntando a quantidade de cigarros fumados por dia e os anos fumando
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você já fumou? "))

# Calculando o total de cigarros fumados no tempo de vida do fumante
# 365 dias por ano * anos fumando para ter o total de dias
dias_fumando = anos_fumando * 365

# A cada cigarro, o fumante perde 10 minutos de vida. 
# Calculando o total de minutos perdidos
minutos_perdidos = cigarros_por_dia * 10 * dias_fumando

# Convertendo minutos perdidos para dias (1 dia = 1440 minutos)
dias_perdidos = minutos_perdidos / 1440

# Exibindo o resultado
print(f"Você perderá {dias_perdidos:.2f} dias de vida.")