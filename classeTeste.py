class Produto:
    def __init__(self,codigo,nome,valor,id=0,estoque=0)-> None:
        self.id = id
        self.codigo = codigo
        self.valor = valor
        self.estoque = estoque

        def incluir(self,valor):
             self.estoque = self.estoque + valor

        def retirar(self, valor):
            if valor <= 0:
                print("Impossivel realizar")
            elif valor > self.estoque:
                print("Sem estoque disponível")
            else:
                self.estoque = self.estoque - valor