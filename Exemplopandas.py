import pandas as pd
import os

def cabeca():
    os.system("cls")
    print("-"*20,end='')
    print("Arquivo Vendas",end='')
    print("-"*20)


vendas_df = pd.read_excel("Vendas.xlsx")
pd.set_option('display.max_columns',None) #mostra todas as colunas

#faturamento por loja
cabeca()
faturamento_loja = vendas_df[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento_loja)


#quantidades de produtos por loja
quantidade_loja = vendas_df[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()


#ticket medio faturamento loja / quantidade por loja
ticket_medio = (faturamento_loja['Valor Final'] /quantidade_loja['Quantidade']).to_frame()


#teste
print("-"*60)
print(quantidade_loja)

print("-"*60)
print(ticket_medio)


