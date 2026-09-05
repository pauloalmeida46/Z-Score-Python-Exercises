# Exercício 5 — Monitoramento de CPU com classificação
# import numpy as np
# cpu = [42, 45, 47, 44, 46, 43, 48, 92]
# Calcule a média e o desvio-padrão.
# Percorra todas as leituras.
# Calcule o Z-Score de cada uma.
# Classifique cada leitura como Comum ou Investigar.
# Mostre o resultado no formato valor -> Z-Score -> classificação.

import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]

# Calculando a média e o desvio-padrão
media = np.mean(cpu)
desvio = np.std(cpu)

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print()

# Percorrendo todas as leituras
for valor in cpu:
    z_score = (valor - media) / desvio

    if abs(z_score) > 3:
        classificacao = "Investigar"
    else:
        classificacao = "Comum"

    print(f"{valor} -> {z_score:.2f} -> {classificacao}")