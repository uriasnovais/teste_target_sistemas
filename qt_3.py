import pandas as pd

dados_1 = open('dados_1.json', 'r').read()  # Read data

df_dados_1 = pd.read_json(dados_1)
df_dados_1_valor_max = df_dados_1['valor'].max()
df_dados_1_media_mes = df_dados_1.mean()

list_dados_1_sem_0 = []
dict_superior_media_mes = {}

for v in df_dados_1['valor']:
    if v != 0:
        list_dados_1_sem_0.append(v)

"""for d, v in df_dados_1['dia'], df_dados_1['valor']:
    if v > df_dados_1_media_mes:
        dict_superior_media_mes[d] = v"""

print(f"O Valor minimo registrado foi {min(list_dados_1_sem_0)}"
      f"\nO Valor máximo registrado foi {df_dados_1_valor_max};")

"""print(dict_superior_media_mes)"""