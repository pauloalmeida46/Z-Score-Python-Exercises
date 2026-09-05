# Exercício 9 — Comparação entre IQR e Z-Score
# import numpy as np
# dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]
# Calcule Q1, Q3 e IQR.
# Calcule os limites inferior e superior do IQR.
# Calcule média e desvio-padrão.
# Calcule o Z-Score do valor 30.
# Compare o que o IQR e o Z-Score indicam sobre o valor 30.
# Escreva uma conclusão curta explicando que técnicas diferentes podem analisar o mesmo dado por
# critérios diferentes.

import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

# Quartis
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)

# IQR
iqr = q3 - q1

# Limites do IQR
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Média e desvio-padrão
media = np.mean(dados)
desvio = np.std(dados)

# Z-Score do valor 30
valor = 30
z_score = (valor - media) / desvio

print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")

print(f"\nMédia: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Z-Score de 30: {z_score:.2f}")

print("\nAnálise do valor 30:")

if valor < limite_inferior or valor > limite_superior:
    print("IQR: 30 é um possível outlier.")
else:
    print("IQR: 30 não é um outlier.")

if abs(z_score) > 3:
    print("Z-Score: 30 merece investigação.")
else:
    print("Z-Score: 30 não ultrapassa o limite de investigação.")

# Conclusão
# O IQR considera 30 um possível outlier, pois ele está acima do limite superior de 17. 
# Já o Z-Score resulta em aproximadamente 2,65, que não ultrapassa o limite de 3.