# Exercício 6 — O mesmo valor em dois contextos
# media_a = 100
# desvio_a = 2
# media_b = 100
# desvio_b = 20
# valor = 110
# Calcule o Z-Score de 110 no Grupo A.
# Calcule o Z-Score de 110 no Grupo B.
# Compare os resultados.
# Explique por que a mesma distância absoluta de 10 unidades pode ser muito incomum em um grupo
# e comum em outro.

media_a = 100
desvio_a = 2

media_b = 100
desvio_b = 20

valor = 110

# Z-Score do Grupo A
z_a = (valor - media_a) / desvio_a

# Z-Score do Grupo B
z_b = (valor - media_b) / desvio_b

print(f"Z-Score no Grupo A: {z_a}")
print(f"Z-Score no Grupo B: {z_b}")

print()
print("Comparação:")
print(f"No Grupo A, 110 está {z_a} desvios-padrão acima da média.")
print(f"No Grupo B, 110 está {z_b} desvio-padrão acima da média.")

# Interpretação
# Nos dois grupos, a distância entre 110 e 100 é exatamente 10 unidades.
# A diferença está no desvio-padrão:

# Grupo	Média	Desvio-padrão	Valor	Z-Score
# A	100	2	110	5,0
# B	100	20	110	0,5

# No Grupo A, os valores costumam ficar muito próximos da média, com desvio de apenas 
# 2 unidades. Por isso, afastar-se 10 unidades é algo enorme: 5 desvios-padrão.

# No Grupo B, os valores são naturalmente mais espalhados, com desvio-padrão de 20. 
# Então, afastar-se 10 unidades representa apenas meio desvio-padrão.

# Conclusão: a mesma diferença absoluta de 10 unidades pode ser muito incomum em um 
# contexto e completamente comum em outro, porque o Z-Score leva em consideração a 
# variabilidade dos dados.