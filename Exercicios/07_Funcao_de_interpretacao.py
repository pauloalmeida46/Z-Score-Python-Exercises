# Exercício 7 — Função de interpretação
# def interpretar_z(z):
# # complete a função
# pass
# valores_z = [-3.5, -1.2, 0, 0.8, 3.7]
# Complete a função para receber um Z-Score.
# Se |Z| > 3, retorne Investigar.
# Se Z < 0, retorne Abaixo da média.
# Se Z > 0, retorne Acima da média.
# Se Z == 0, retorne Na média.
# Teste a função com todos os valores fornecidos.

def interpretar_z(z):
    if abs(z) > 3:
        return "Investigar"
    elif z < 0:
        return "Abaixo da média"
    elif z > 0:
        return "Acima da média"
    else:
        return "Na média"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

for z in valores_z:
    resultado = interpretar_z(z)
    print(f"{z} -> {resultado}")