#fase 1- conexão

import pymysql
import os

conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    password = 'fbradesco',
    database='dbloja'
    

)
with conexao:
    with conexao.cursor() as cursor:
    
        TABLE_NAME='produto'

        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
            'id INT AUTO_INCREMENT PRIMARY KEY,'
            'nome VARCHAR(50) NOT NULL,'
            'valor double(10,2) NOT NULL,'
            'quantidade INT NOT NULL'
            
            ')'
        )
    conexao.commit()

    with conexao.cursor() as cursor:
        TABLE_NAME='cliente'
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
            'id INT AUTO_INCREMENT PRIMARY KEY,'
            'nome VARCHAR(50) NOT NULL,'
            'cpf VARCHAR(11),'
            'telefone VARCHAR(20),'
            'email varchar(50)'
            ')'
        )
    conexao.commit()

    #LISTANDO 
    with conexao.cursor() as cursor:
        TABLE_NAME= input("Digite o nome da tabela : ")

        sql = f'SELECT * FROM {TABLE_NAME}'

        cursor.execute(sql)
        
        resposta = cursor.fetchall()

        print(resposta)

        #inserindo dados em produto
        sql = f'INSERT INTO produto(nome,valor,quantidade) values("CAMISA",50.50,10)'
        cursor.execute(sql)
        conexao.commit()
        
        sql = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(sql)
        resposta = cursor.fetchall()
        print(resposta)
        conexao.commit()