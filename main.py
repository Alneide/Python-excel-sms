import pandas as pd

# passo a passo

# Abrir os 6 arquivos em Excel
Lista_meses = ['janeiro', 'fevereiro', 'março','abril',"maio", "junho"]

for mes in lista_meses :
    print(mes)
    tabela_vendas = pd.read_excel (f"{mes}.xlsx")
    print (tabela_vendas)