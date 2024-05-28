import pandas as pd
import matplotlib.pyplot as plt
import os



pd.set_option('display.max_columns', None)

#lendo a base de dados em um objeto
df = pd.read_csv('Feminicidio.csv')

cidades = [
    'Santo André',
    'São Bernardo do Campo',
    'São Caetano do Sul',
    'Mauá',
    'Diadema',
    'Rio Grande da Serra',
    'Ribeirão Pires'
]

#montagem imagem de Osasco
# cidade_df = df[df['MUNICIPIO_CIRCUNSCRICAO']=='Osasco']
cidade_df = df[df['MUNICIPIO_CIRCUNSCRICAO'].isin(cidades)]


#grupoby da vitimas
cidade_vitimas_df = cidade_df[['MUNICIPIO_CIRCUNSCRICAO', 'VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum().reset_index(names='CIDADE')
cidade_vitimas_df = cidade_vitimas_df.sort_values(by='VITIMAS',ascending=False)

#montando o grupo by de raça
raca_df = cidade_df.groupby('COR_PELE').size().reset_index(name="QUANTIDADE")
raca_df = raca_df.sort_values(by='COR_PELE',ascending=True)

os.system('cls') # os.system('clear')

print("-"*20)
print("Analise por cidade")
print(cidade_vitimas_df)

print("-"*20)
print("Analise por cidade x raça")
print(raca_df)

#gerando a pizza dos municipios
plt.figure(figsize=(8,8))
plt.pie(cidade_vitimas_df['VITIMAS'], labels=cidade_vitimas_df['CIDADE'], autopct='%1.1f%%', startangle=140)
plt.title('VITIMAS NO ABC PAULISTA')
plt.axis("equal")
plt.show()

# Gerar um gráfico linhas verticais
plt.figure(figsize=(10, 6))
plt.barh(cidade_vitimas_df['CIDADE'], cidade_vitimas_df['VITIMAS'])
plt.xlabel('CIDADES ABCDMR')
plt.ylabel('Quantidade de Vítimas')
plt.title('Quantidade de Vítimas ABCDMR')
plt.gca().invert_yaxis() 
# plt.xticks(rotation=90)
plt.show()

