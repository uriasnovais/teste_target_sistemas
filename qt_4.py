#calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

import pandas as pd

dic_faturamento_mensal = {'SP': 67836.43,
                          'RJ': 36678.66,
                          'MG': 29229.88,
                          'ES': 27165.48,
                          'Outros': 19849.53}

dt_faturamento_mensal = pd.DataFrame.from_dict(dic_faturamento_mensal, orient='index')
dt_faturamento_mensal.reset_index(inplace=True)
dt_faturamento_mensal.rename(columns={'index': 'estado', 0: 'faturamento'}, inplace=True)
#linha que calcula a porcentagem de cada estado e adiciona ao data frame
dt_faturamento_mensal['porcentagem'] = ((dt_faturamento_mensal['faturamento'] / dt_faturamento_mensal['faturamento'].sum()) * 100)

#Printa o data frame completo onde podemos visualizar o percentual na ultima coluna
print(dt_faturamento_mensal)
