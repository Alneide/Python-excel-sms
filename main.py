import pandas as pd
from twilio.rest import Client

# passo a passo

# Abrir os 6 arquivos em Excel
Lista_meses = ['janeiro', 'fevereiro', 'março','abril',"maio", "junho"]

for mes in lista_meses :
    tabela_vendas = pd.read_excel (f"{mes}.xlsx")
    if (tabela_vendas["vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela - vendas["vendas"] > 55000, "Vendas"].values[0]

    print (f"No mês{mes} alguém bateu a meta. Vendedor:  {Vendedor}, Vendas: {Vendas}")

 
    # Your Account SID from twilio.com/console
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # Your Auth Token from twilio.com/console
    auth_token = "your_auth_token"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")

    print(message.sid)


