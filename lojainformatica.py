while True:
    op = input("[i]nserir\n[a]adicionar\n[d]deletar\n[s]air\n [c]clear\n Digite a letra da sua opção: ").lower()
    

class Cliente:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Loja:
    def __init__(self):
        self.clientes = []
        self.produtos = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
        

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print("Produto adicionado com sucesso!")

    def listar_produtos(self):
        print("Produtos disponíveis:")
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco} - Estoque: {produto.estoque}")

    def comprar_produto(self, cliente, produto, quantidade):
        if produto in self.produtos:
            if produto.estoque >= quantidade:
                print(f"Compra realizada! Total: R${produto.preco * quantidade}")
                produto.estoque -= quantidade
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não disponível na loja.")

# Exemplo de uso:
if __name__ == "__main__":
    loja = Loja()

    # Cadastro de clientes
    cliente1 = Cliente("João", "joao@example.com", "Rua A, 123")
    loja.adicionar_cliente(cliente1)

    # Cadastro de produtos
    produto1 = Produto("Notebook", 2500, 10)
    produto2 = Produto("Mouse", 50, 20)
    loja.adicionar_produto(produto1)
    loja.adicionar_produto(produto2)

    # Listar produtos
    loja.listar_produtos()

    # Compra de produtos
    loja.comprar_produto(cliente1, produto1, 2)
    loja.comprar_produto(cliente1, produto2, 3)

    # Listar produtos após a compra
    loja.listar_produtos()
