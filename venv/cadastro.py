# fase 1 - conexão
import pymysql
import os

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='dbloja'
   )

with conexao:
    with conexao.cursor() as cursor:
        TABLE_NAME = 'produto'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'nome VARCHAR(50) NOT NULL, '
            'valor DOUBLE(10,2) NOT NULL,'
            'quantidade INT NOT NULL'
            ')'
        )
    conexao.commit()

    with conexao.cursor() as cursor:
        TABLE_NAME = 'cliente'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'nome VARCHAR(50) NOT NULL, '
            'cpf VARCHAR(11) ,'
            'telefone VARCHAR(20) ,'
            'email VARCHAR(50)'
            ')'
        )
    conexao.commit()

    op = input("1 - cadastro de produto\n2 - Cadastro de cliente\n3 - Selecionar um produto : ")
    if op == '1':
        #LISTANDO A BAGAÇA
        with conexao.cursor() as cursor:
            print("INICIANDO A TABELA")
            TABLE_NAME = input("Digite o nome da tabela :").lower()
            
            sql =f'SELECT * FROM {TABLE_NAME}'
            cursor.execute(sql)
            resposta = cursor.fetchall()
            print(resposta)

            #inserindo dados em produto
            nome = input("Digite o nome do produto : ").upper()
            valor = float(input("Digita o valor do produto :"))
            quantidade = int(input("Digite a quantidade em estoque do produto : "))
            dados = (nome,valor,quantidade)
            sql = f'INSERT INTO {TABLE_NAME} (nome, valor, quantidade) VALUES (%s,%s,%s)'
            cursor.execute(sql,dados)
            conexao.commit()

            sql =f'SELECT * FROM {TABLE_NAME}'
            cursor.execute(sql)
            resposta = cursor.fetchall()
            
            for linha in resposta:
                print(linha)
        conexao.commit()
    elif op == '2':
        with conexao.cursor() as cursor:
            #inserindo dados em cliente
            sql =f'SELECT * FROM {TABLE_NAME}'
            cursor.execute(sql)
            resposta = cursor.fetchall()
            print(resposta)

            TABLE_NAME = 'cliente'
            nome = input("Digite o nome do cliente : ").upper()
            cpf = input("Digite o CPF : ")
            telefone = input("Digite o telefone : ")
            email = input("Digite o email : ")
            dados = (nome, cpf, telefone, email)
            sql = f'INSERT INTO {TABLE_NAME} (nome, cpf, telefone, email) VALUES (%s,%s,%s,%s)'
            cursor.execute(sql,dados)
            conexao.commit()

            sql =f'SELECT * FROM {TABLE_NAME}'
            cursor.execute(sql)
            resposta = cursor.fetchall()
            
            for linha in resposta:
                print(linha) 
        conexao.commit()
    elif op == '3':
         with conexao.cursor() as cursor:
            print("LISTANDO PRODUTOS")
            TABLE_NAME = 'produto'
            
            nome = input('Digite o nome do produto :')
            dados = (nome)
            sql =f'SELECT * FROM {TABLE_NAME} WHERE nome=%s'
            cursor.execute(sql,dados)
            resposta = cursor.fetchall()
            print(resposta)
    else:
        print("Opção invalida")

