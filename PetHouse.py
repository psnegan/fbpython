import pymysql
import os
import time

# Classe Produto
class Produto:
    def __init__(self, codigo, nome, valor, estoque):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return f'Codigo: {self.codigo}, Nome: {self.nome}, Valor: R${self.valor}, Estoque: {self.estoque}'

# Classe Usuarios
class Usuarios:
    def __init__(self, email, senha):
        self.id = None  # Inicialmente None, será atribuído depois
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'ID: {self.id}, Email: {self.email}'

# Classe PetHouse
class PetHouse:
    def __init__(self, produtopet, senha, descricao, fornecedor, valor, estoque):
        self.produtopet = produtopet
        self.senha = senha
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.valor = valor
        self.estoque = estoque

    def incluir(self, quantidade):
        if quantidade <= 0:
            print("Quantidade deve ser positiva e menor ou igual a 45.")
        elif self.estoque + quantidade > 45:
            print("Superou o estoque máximo. Digite um valor abaixo de 45.")
        else:
            self.estoque += quantidade
            print("Inserido no estoque. Cadastrado com sucesso.")

    def retirar(self, quantidade):
        if quantidade <= 0:
            print("Quantidade deve ser positiva.")
        elif quantidade > self.estoque:
            print("Estoque insuficiente.")
        else:
            self.estoque -= quantidade
            print("Retirado do estoque com sucesso.")

    def __str__(self):
        return f'Produto: {self.produtopet}, Descrição: {self.descricao}, Fornecedor: {self.fornecedor}, Valor: R${self.valor}, Estoque: {self.estoque}'

# Função para limpar a tela
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conexão com o banco de dados
con = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='pethouse'
)

# Criação das tabelas no banco de dados
with con:
    with con.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto (
                codigo INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50),
                valor FLOAT,
                estoque INT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(50),
                senha VARCHAR(50)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pethouse (
                codigo INT AUTO_INCREMENT PRIMARY KEY,
                descricao VARCHAR(100),
                fornecedor VARCHAR(50),
                valor FLOAT,
                estoque INT
            )
        ''')
        con.commit()

# Verificação de senha especial
def verificar_senha_especial(senha):
    senha_especial = "123456"  # Defina a senha especial aqui
    return senha == senha_especial

# Função de autenticação
def autenticar(email, senha):
    with con.cursor() as cursor:
        cursor.execute('SELECT id, email, senha FROM usuario WHERE email=%s AND senha=%s', (email, senha))
        usuario = cursor.fetchone()
        if usuario:
            user = Usuarios(usuario[1], usuario[2])
            user.id = usuario[0]
            return user
        return None

# Verificação de email especial
def verificar_email_especial(email):
    email_especial = "epa10@gmail.com"  # Defina o email especial aqui
    return email == email_especial

# Solicitação de login
def login():
    while True:
        limpaTela()
        print("LOGIN")
        email = input("Email: ")
        senha = input("Senha: ")
        if verificar_email_especial(email):  # Verifica o email especial
            if verificar_senha_especial(senha):  # Verifica a senha especial
                print("Login bem-sucedido!")
                time.sleep(1)
                return Usuarios(email, senha)
            else:
                print("Senha incorreta. Tente novamente.")
                time.sleep(2)
        else:
            usuario = autenticar(email, senha)
            if usuario:
                print("Login bem-sucedido!")
                time.sleep(1)
                return usuario
            else:
                print("Email ou senha incorretos. Tente novamente.")
                time.sleep(2)


# Programa principal - CRUD
def main():
    while True:
        limpaTela()
        print("1 - Cadastrar Produto")
        print("2 - Alterar Produto")
        print("3 - Listar Produtos")
        print("4 - Excluir Produto")
        print("5 - Movimentar Estoque")
        print("6 - Sair")
        
        op = input("Digite a opção desejada: ")
        
        with con.cursor() as cursor:
            if op == '6':
                print("Até breve...")
                time.sleep(2)
                break

            elif op == '1':
                print("-" * 20)
                print("CADASTRAMENTO")
                nome = input("Digite o nome do produto: ")
                valor = float(input("Digite o valor do produto: R$ "))
                while True:
                    estoque = int(input("Digite a quantidade em estoque (máximo 45 unidades): "))
                    if estoque > 45:
                        print("Quantidade em estoque não pode exceder 45 unidades. Tente novamente.")
                    else:
                        break
                cursor.execute('''
                    INSERT INTO produto (nome, valor, estoque) 
                    VALUES (%s, %s, %s)
                ''', (nome, valor, estoque))
                con.commit()
                print("PRODUTO CADASTRADO")
                time.sleep(1)

            elif op == '2':
                print("-" * 20)
                print("ALTERAÇÃO")
                codigo = input("Digite o código do produto a ser alterado: ")
                novo_nome = input("Informe o novo nome do produto: ")
                novo_valor = float(input("Digite o novo valor do produto: R$ "))
                novo_estoque = int(input("Digite a nova quantidade em estoque: "))
                cursor.execute('''
                    UPDATE produto 
                    SET nome=%s, valor=%s, estoque=%s 
                    WHERE codigo=%s

                ''', (novo_nome, novo_valor, novo_estoque, codigo))
                con.commit()
                print("PRODUTO ALTERADO")
                time.sleep(1)

            elif op == '3':
                print("-" * 20)
                print("LISTAGEM")
                cursor.execute('SELECT * FROM produto')
                resposta = cursor.fetchall()
                for linha in resposta:
                    print(f'Codigo: {linha[0]}, Nome: {linha[1]}, Valor: R${linha[2]}, Estoque: {linha[3]}')
                time.sleep(3)

            elif op == '4':
                print("-" * 20)
                print("EXCLUSÃO")
                codigo = input("Digiteo código do produto a ser excluído: ")
                cursor.execute('DELETE FROM produto WHERE codigo=%s', (codigo,))
                con.commit()
                print("PRODUTO EXCLUÍDO")
                time.sleep(1)

            elif op == '5':
                print("-" * 20)
                print("MOVIMENTAÇÃO")
                codigo = input("Digite o código do produto a ser movimentado: ")
                cursor.execute('SELECT * FROM produto WHERE codigo=%s', (codigo,))
                item = cursor.fetchone()
                if item:
                    produto_item = Produto(*item)
                    print(produto_item)
                    movimento = int(input("Digite a quantidade a ser movimentada (positiva para entrada, negativa para saída): "))
                    novo_estoque = produto_item.estoque + movimento
                    if movimento <= 0:
                        print("Quantidade deve ser positiva.")
                    elif novo_estoque > 45:
                        print("Estoque total não pode exceder 45 unidades. Operação não permitida.")
                    elif novo_estoque < 0:
                        print("Estoque insuficiente.")
                    else:
                        cursor.execute('UPDATE produto SET estoque=%s WHERE codigo=%s', (novo_estoque, codigo))
                        con.commit()
                        print("ESTOQUE ATUALIZADO")
                else:
                    print("Produto não encontrado!")
                time.sleep(3)

print("Programa encerrado.")

# Loop de login
usuario_atual = None
while not usuario_atual:
    usuario_atual = login()

# Executa o programa principal após login bem-sucedido
main()
