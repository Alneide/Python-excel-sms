import pandas as pd
from twilio.rest import Client

account_sid = "AC631b9361e8b67690bcdc1c53a4558624"
# Your Auth Token from twilio.com/console
auth_token = "26fb818d42b70fc98298209616c7318b"
client = Client(account_sid, auth_token)

# passo a passo

# Abrir os 6 arquivos em Excel
Lista_meses = ['janeiro', 'fevereiro', 'março','abril',"maio", "junho"]

for mes in lista_meses :
    tabela_vendas = pd.read_excel (f"{mes}.xlsx")
    if (tabela_vendas["vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendas"].values[0]

    print (f"No mês{mes} alguém bateu a meta. Vendedor:  {Vendedor}, Vendas: {Vendas}")

    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")

    print(message.sid)


