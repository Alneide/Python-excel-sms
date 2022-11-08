import pandas as pd

# passo a passo

# Abrir os 6 arquivos em Excel
Lista_meses = ['janeiro', 'fevereiro', 'março','abril',"maio", "junho"]

for mes in lista_meses :
    tabela_vendas = pd.read_excel (f"{mes}.xlsx")
    if (tabela_vendas["vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendas"].values[0]

    print (f"No mês{mes} alguém bateu a meta. Vendedor:  {Vendedor}, Vendas: {Vendas}")


