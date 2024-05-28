import pandas as pd
import os
def cabeca():
    os.system("cls")
    print("-"*20,end='')
    print("Arquivo Feminicidio",end='')
    print("-"*20)
pd.set_option('display.max_columns',None)
fem_df = pd.read_csv("Feminicidio.csv")

print(fem_df)

#quantidade anual

anual=fem_df[['ANO_ESTATISTICA','VITIMAS']].groupby('ANO_ESTATISTICA').sum()
print(anual)
 
#raça

