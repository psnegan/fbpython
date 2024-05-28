import pymysql
import os
import time

# Função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função para criar tabelas
def criar_tabelas(cursor):
    tabelas = {
        "Poupanca": (
            'id INT AUTO_INCREMENT PRIMARY KEY, '
            'numero INT NOT NULL, '
            'cpf VARCHAR(20) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL, '
            'ativa BOOL, '
            'diaAniversarioPoupanca INT NOT NULL'
        ),
        "Corrente": (
            'id INT AUTO_INCREMENT PRIMARY KEY, '
            'numero INT NOT NULL, '
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL, '
            'ativa BOOL, '
            'contadorTalao INT NOT NULL'
        ),
        "Especial": (
            'id INT AUTO_INCREMENT PRIMARY KEY, '
            'numero INT NOT NULL, '
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL, '
            'ativa BOOL, '
            'limite DOUBLE(10,2) NOT NULL'
        )
    }
    
    for tabela, estrutura in tabelas.items():
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabela} ({estrutura})')

# Função para cadastrar conta poupança
def cadastrar_poupanca(cursor):
    limpar_tela()
    print("BANK - CONTA POUPANÇA - CADASTRAR")
    numero = int(input("Digite o numero da conta: "))
    cpf = input("Digite o CPF do cliente da conta: ")
    dia_aniversario_conta = int(input("Digite o dia de aniversário da conta: "))
    dados = (numero, cpf, 0.00, 1, dia_aniversario_conta)
    sql = f'INSERT INTO Poupanca (numero, cpf, saldo, ativa, diaAniversarioPoupanca) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(sql, dados)
    print("Dados cadastrados com sucesso!")

# Função para alterar conta poupança
def alterar_poupanca(cursor):
    limpar_tela()
    print("BANK - CONTA POUPANÇA - ALTERAR")
    numero = int(input("Digite o numero da conta a ser alterada: "))
    novo_cpf = input("Digite o novo CPF do cliente: ")
    novo_dia_aniversario = int(input("Digite o novo dia de aniversário da conta: "))
    sql = f'UPDATE Poupanca SET cpf = %s, diaAniversarioPoupanca = %s WHERE numero = %s'
    cursor.execute(sql, (novo_cpf, novo_dia_aniversario, numero))
    print("Dados alterados com sucesso!")

# Função para apagar conta poupança
def apagar_poupanca(cursor):
    limpar_tela()
    print("BANK - CONTA POUPANÇA - APAGAR")
    numero = int(input("Digite o numero da conta a ser apagada: "))
    sql = f'DELETE FROM Poupanca WHERE numero = %s'
    cursor.execute(sql, (numero,))
    print("Conta apagada com sucesso!")

# Função para movimentar conta poupança
def movimentar_poupanca(cursor):
    limpar_tela()
    print("BANK - CONTA POUPANÇA - MOVIMENTAR")
    numero = int(input("Digite o numero da conta: "))
    movimento = input("Digite 'D' para depósito ou 'S' para saque: ").upper()
    valor = float(input("Digite o valor: "))
    
    if movimento == 'D':
        sql = f'UPDATE Poupanca SET saldo = saldo + %s WHERE numero = %s'
        cursor.execute(sql, (valor, numero))
        print(f'Depósito de {valor} realizado com sucesso!')
    elif movimento == 'S':
        sql = f'SELECT saldo FROM Poupanca WHERE numero = %s'
        cursor.execute(sql, (numero,))
        saldo_atual = cursor.fetchone()[0]
        if saldo_atual >= valor:
            sql = f'UPDATE Poupanca SET saldo = saldo - %s WHERE numero = %s'
            cursor.execute(sql, (valor, numero))
            print(f'Saque de {valor} realizado com sucesso!')
        else:
            print("Saldo insuficiente para saque.")
    else:
        print("Movimento inválido, por favor digite 'D' para depósito ou 'S' para saque.")

def main():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='fbradesco',
        database='bank'
    )

    with conexao:
        with conexao.cursor() as cursor:
            criar_tabelas(cursor)
        conexao.commit()

        while True:
            limpar_tela()
            print('-'*80)
            print("BANK")
            print('-'*80)
            print("1 - Poupança")
            print("2 - Corrente")
            print("3 - Especial")
            print("4 - Sair")
            opcao_menu_principal = input("Digite sua opção: ")
            if opcao_menu_principal == '4':
                break
            elif opcao_menu_principal == '1':
                while True:
                    limpar_tela()
                    print('-'*80)
                    print("BANK - CONTA POUPANÇA")
                    print('-'*80)
                    print("1 - Cadastrar")
                    print("2 - Alterar")
                    print("3 - Apagar")
                    print("4 - Movimentar")
                    print("5 - Sair")
                    sub_opcao_menu = input("Digite sua opção: ")
                    if sub_opcao_menu == '5':
                        break
                    elif sub_opcao_menu == '1':
                        with conexao.cursor() as cursor:
                            cadastrar_poupanca(cursor)
                        conexao.commit()
                        time.sleep(3)
                    elif sub_opcao_menu == '2':
                        with conexao.cursor() as cursor:
                            alterar_poupanca(cursor)
                        conexao.commit()
                        time.sleep(3)
                    elif sub_opcao_menu == '3':
                        with conexao.cursor() as cursor:
                            apagar_poupanca(cursor)
                        conexao.commit()
                        time.sleep(3)
                    elif sub_opcao_menu == '4':
                        with conexao.cursor() as cursor:
                            movimentar_poupanca(cursor)
                        conexao.commit()
                        time.sleep(3)

if __name__ == "__main__":
    main()
