# Exercício 8 — Z-Score em um DataFrame
# import pandas as pd
# import numpy as np
# dados = {
# "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
# "Requisicoes": [120, 135, 128, 122, 130, 400]
# }
# df = pd.DataFrame(dados)
# Calcule a média da coluna Requisicoes.
# Calcule o desvio-padrão da coluna.
# Crie a coluna Z_Score.
# Crie a coluna Status com os valores Comum ou Investigar.
# Exiba apenas as linhas marcadas para investigação.

import pandas as pd
import numpy as np

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400]
}

df = pd.DataFrame(dados)

# Calculando a média
media = df["Requisicoes"].mean()

# Calculando o desvio-padrão
desvio = df["Requisicoes"].std()

# Criando a coluna Z_Score
df["Z_Score"] = (df["Requisicoes"] - media) / desvio

# Criando a coluna Status
df["Status"] = np.where(
    abs(df["Z_Score"]) > 3,
    "Investigar",
    "Comum"
)

# Exibindo média e desvio-padrão
print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")

# Exibindo o DataFrame completo
print("\nDataFrame:")
print(df)

# Exibindo apenas as linhas para investigação
print("\nLinhas para investigação:")
print(df[df["Status"] == "Investigar"])