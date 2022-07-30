"""Encontrar o menor e o maior valor ocorrido no mês desconsiderando o 0,
e o número de dias nos quais o valor foi superior à média"""

import pandas as pd

dados_1 = open('dados_1.json', 'r').read()  # Read data

df_dados_1 = pd.read_json(dados_1)
df_dados_1_media_mes = df_dados_1.query('`valor` > 0').mean()

print(f"O Faturamento minimo registrado diferente de 0 foi R$ {df_dados_1.query('`valor` > 0').min()['valor']}"
      f"\nO Faturamento máximo registrado foi R$ {df_dados_1['valor'].max()};")

query = df_dados_1.query(f"`valor` >= {df_dados_1_media_mes['valor']}")
total_dias_acima_media = 0

for d in query['dia']:
    total_dias_acima_media += 1

print(f"O total de dias nos quais o Faturamento é superior a média, R$ {df_dados_1_media_mes['valor']:.4f}, são {total_dias_acima_media};")

#Printar a query mostrando somente os dias superiores a média
#print(query)
