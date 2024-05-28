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

# Exemplo de uso
pethouse = PetHouse('Ração para Cães', '1234', 'Ração premium para cães', 'Fornecedor X', 120.00, 20)
print(pethouse)
pethouse.incluir(10)
print(pethouse)
pethouse.retirar(5)
print(pethouse)
pethouse.incluir(50)  # Deve falhar porque excede o limite de 45
pethouse.retirar(30)
print(pethouse)
