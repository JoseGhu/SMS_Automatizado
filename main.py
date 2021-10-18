import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2214fa0193e94e3984b1e84d0ef7822e"
# Your Auth Token from twilio.com/console
auth_token = "42835c6d9bf8db9f50dd44509cc6dc83"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas ['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas} Desenvolvido por DevGhu')
        message = client.messages.create(
            to="+5511969224529",
            from_="+15074282837",
            body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)




# Para cada arquivo:

# Verificar se algum valor na quela tabela na coluna de vendas é maior que R$ 55.000,00.

# Se for maior de R$ 55.000,00 envia um SMS com o Nome, mes e as vendas dele.

# caso nao seja maior mao quero fazer nada.


