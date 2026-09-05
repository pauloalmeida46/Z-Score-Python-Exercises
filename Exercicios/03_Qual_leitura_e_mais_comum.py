# Exercício 3 — Qual leitura é mais incomum?
# temperaturas = [21, 23, 25, 27, 29]
# media = 25
# desvio = 2
# Calcule o Z-Score de cada temperatura.
# Identifique qual valor está mais distante da média em termos de desvio-padrão.
# Mostre qual possui o maior valor absoluto de Z

temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

for temperatura in temperaturas:
    z_score = (temperatura - media) / desvio
    valor_absoluto = abs(z_score)

    print(f"Temperatura: {temperatura} | Z-Score: {z_score} | |Z|: {valor_absoluto}")

# Qual é a mais incomum?
# As temperaturas 21°C e 29°C são as mais distantes da média, pois ambas possuem:
# $$ |Z| = 2 $$
# Ou seja, estão 2 desvios-padrão de distância da média.