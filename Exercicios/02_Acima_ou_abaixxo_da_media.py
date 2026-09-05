# Exercício 2 — Acima ou abaixo da média?
# casos = [85, 100, 120]
# media = 100
# desvio = 10
# Calcule o Z-Score dos três valores.
# Para cada resultado, informe se o valor está abaixo da média, exatamente na média ou acima da
# média.
# Explique o que significa o sinal positivo, negativo ou zero.

casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z_score = (valor - media) / desvio

    if z_score < 0:
        situacao = "abaixo da média"
    elif z_score == 0:
        situacao = "exatamente na média"
    else:
        situacao = "acima da média"

    print(f"Valor: {valor} | Z-Score: {z_score} | {situacao}")

# Interpretação do sinal
# Z negativo (-) → o valor está abaixo da média.
# Z igual a zero (0) → o valor está exatamente na média.
# Z positivo (+) → o valor está acima da média.