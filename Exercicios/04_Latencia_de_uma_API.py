# Exercício 4 — Latência de uma API
# import numpy as np
# latencias = [98, 102, 101, 99, 100, 103, 97, 180]
# Calcule a média e o desvio-padrão do conjunto.
# Calcule somente o Z-Score da latência 180 ms.
# Informe se esse valor merece investigação usando |Z| > 3.
# Mostre uma mensagem lembrando que investigar não significa apagar automaticamente.

import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

# Calculando a média
media = np.mean(latencias)

# Calculando o desvio-padrão
desvio = np.std(latencias)

# Calculando o Z-Score somente da latência 180
valor = 180
z_score = (valor - media) / desvio

print(f"Média: {media:.2f} ms")
print(f"Desvio-padrão: {desvio:.2f} ms")
print(f"Z-Score de 180 ms: {z_score:.2f}")

if abs(z_score) > 3:
    print("A latência de 180 ms merece investigação.")
else:
    print("A latência de 180 ms não ultrapassa o limite de investigação (|Z| > 3).")

print("Investigar um possível outlier não significa apagá-lo automaticamente.")