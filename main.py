import pandas as pd

# passo a passo

# Abrir os 6 arquivos em Excel
Lista_meses = ['janeiro', 'fevereiro', 'março','abril',"maio", "junho"]

for mes in lista_meses :
    tabela_vendas = pd.read_excel (f"{mes}.xlsx")
    if (tabela_vendas["vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendedor"]
        vendas = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendas"]

    print (f"No mês{mes}encontrou alguém com mais de 55000")

