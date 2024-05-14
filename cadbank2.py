# fase 1 - conexão
import pymysql
import os
import time


conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='bank'
   )

os.system("cls")

with conexao:
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Poupanca'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(20) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'diaAniversarioPoupanca INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Corrente'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'contadorTalao INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Especial'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'limite double(10,2) NOT NULL'
            ')'
        )
    conexao.commit()    

    #MONTAGEM DO MENU DE ACESSO
    while True:
        os.system("cls")
        print('-'*80)
        print("BANK")
        print('-'*80)
        print("1 - Poupança")
        print("2 - Corrente")
        print("3 - Especial")
        print("4 - Sair")
        opcao_menu_principal=input("Digite sua opção :")
        if opcao_menu_principal=='4':
            break
        elif opcao_menu_principal=='1':
            while True:
                os.system("cls")
                print('-'*80)
                print("BANK - CONTA POUPANÇA")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dia_aniversario_conta = int(input("Digite o dia de aniversario da conta : "))
                        dados = (numero, cpf, 0.00, 1, dia_aniversario_conta)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, diaAniversarioPoupanca) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

