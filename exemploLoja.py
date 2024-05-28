import pymysql
import os
import time
from classeTeste import Produto

def limpaTela():
    os.system('cls')

limpaTela()
#criar o banco de dados
con = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='dbloja'
)

with con:
    with con.cursor() as cursor:
        TABLE_NAME = "produto"
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
                       'ID INT AUTO_INCREMENT PRIMARY KEY ,'
                       'CODIGO VARCHAR(10) NOT NULL ,'
                       'NOME VARCHAR(50) NOT NULL ,'
                       'VALOR DOUBLE(10,2) ,'
                       'ESTOQUE INT NOT NULL'
        ')')
        con.commit()
    #programa pricipal - crud
    with con.cursor() as cursor:
        while True:
            limpaTela()
            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Listar")
            print("4 - Excluir")
            print("5 - Movimento")
            print("6 - Sair")
            op = input("Escolha o numero da sua opção: ")
            
            if op=='6':
                time.sleep(2)
                print("Até breve...")
                break
            
            elif op == '1':
                print("-"*20)
                print("CADASTRAMENTO")
                codigo = input('Digite o codigo : ')
                nome = input("Digite o Nome produto : ")
                valor = float(input("Digite o valor do produto : R$ "))
                item = Produto(codigo,nome,valor)
                cursor.execute(f'INSERT INTO PRODUTO (CODIGO,NOME,VALOR,ESTOQUE) '\
                'VALUES (%s,%s,%s,%s)',(item.codigo,item.nome, item.valor,item.estoque))
                con.commit()
                print("PRODUTO CADASTRADO")
                time.sleep(1)
            elif op == '2':
                print("-"*20)
                print("ALTERAÇÃO")
                codigo = input("Digite o codigo do produto a ser alterado : ")
                nome= input("Informe o novo nome do produto : ")
                valor = float(input("Digite o novo valor do produto : "))
                item = Produto(codigo,nome,valor)
                cursor.execute(f'UPDATE PRODUTO SET NOME=%s, VALOR=%s WHERE CODIGO=%s',(item.nome,item.valor,item.codigo))
                con.commit()
                time.sleep(1)
            elif op=='3':
                print("-"*20)
                print("LISTAGEM")
                cursor.execute('SELECT * FROM PRODUTO')
                resposta = cursor.fetchall()
                for linha in resposta:
                    print(linha)
                time.sleep(3)
            elif op== '4':
                print("-"*20)
                print("LISTAGEM")
                codigo = input("Digite o codigo do produto a ser excluido : ")
                cursor.execute(f'DELETE FROM PRODUTO WHERE CODIGO=%s',(codigo))
                con.commit()
                print("Produto deletado...")
                time.sleep(1)
            elif op=='5':
                print("-"*20)
                print("MOVIMENTAÇÃO")
                codigo = input("Digite o codigo do produto a ser movimentado : ")
                cursor.execute(f'SELECT * FROM PRODUTO WHERE CODIGO=%s',(codigo))
                item = cursor.fetchone()
                produto_item = Produto(*item)
                print(produto_item)
                time.sleep(5)
                
                
                
                

    class Produto:
        def __init__(self,codigo,nome,valor,id=0,estoque=0):
            self.id = id
            self.codigo = codigo
            self.nome = nome
            self.valor = valor
            self.estoque = estoque

    def incluir(self,valor):
        self.estoque = self.estoque + valor
    
    def retirar(self, valor):
        if valor <= 0:
            print("impossivel realizar")
        elif valor > self.estoque:
            print("Sem estoque disponivel")
        else:
            self.estoque = self.estoque - valor

    def __str__(self):
        return f'Id : {self.id} - cod : {self.codigo} - nome : {self.nome} - valor R$ : {self.valor} - estoque : {self.estoque}'


     
     
                
