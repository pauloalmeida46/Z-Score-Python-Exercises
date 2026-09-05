# Exercício 10 — Mini análise de eventos de segurança
# import pandas as pd
# dados = {
# "Evento": ["A", "B", "C", "D", "E", "F", "G"],
# "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
# }
# df = pd.DataFrame(dados)
# Calcule a média de Tentativas_Login.
# Calcule o desvio-padrão.
# Calcule o Z-Score de cada evento.
# Identifique eventos com |Z| > 3.
# Mostre uma mensagem final explicando por que um evento incomum em segurança pode ser
# justamente o dado mais importante da análise.

import pandas as pd
import numpy as np

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
}

df = pd.DataFrame(dados)

# Média
media = np.mean(df["Tentativas_Login"])

# Desvio-padrão
desvio = np.std(df["Tentativas_Login"])

# Z-Score de cada evento
df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")

print("\nZ-Score dos eventos:")
print(df)

# Identificando eventos com |Z| > 3
investigar = df[abs(df["Z_Score"]) > 3]

print("\nEventos com |Z| > 3:")
print(investigar)

print("\nMensagem final:")
print("Em segurança, um evento incomum pode ser justamente o dado mais importante,")
print("pois ele pode indicar uma tentativa de ataque ou um comportamento suspeito.")