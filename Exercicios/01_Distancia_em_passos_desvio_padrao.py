# Exercício 1 — Distância em passos de desvio-padrão
# media = 100
# desvio = 5
# valor = 115
# Calcule a distância entre o valor e a média.
# Descubra quantos desvios-padrão cabem nessa distância.
# Mostre o Z-Score.
# Exiba uma frase interpretando o resultado em linguagem natural.

media = 100
desvio = 5
valor = 115

# Distância entre o valor e a média
distancia = valor - media

# Quantos desvios-padrão existem nessa distância
passos_desvio = distancia / desvio

# Z-Score
z_score = (valor - media) / desvio

print("Distância entre o valor e a média:", distancia)
print("Quantidade de desvios-padrão:", passos_desvio)
print("Z-Score:", z_score)

print(f"O valor {valor} está {z_score} desvios-padrão acima da média.")