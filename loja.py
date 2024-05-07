lista_prod = []
lista_carrinho = []
def cadastrar():
    sair = False
    while sair==False:
        print("da as ideia: ")
        print("Cadastrar\nExcluir\nListar\nSair")
            
        try:
            op = input("Digite a inicial da opção que deseja: ").upper()
        except:
            print("Fio, não é tão difícil, digita certo.")

        if(op == "C"):
            try:
                desc = input("Descrição: ")
                valor = float(input("Valor: "))
                produto = {
                    "Descrição": desc,
                    "Valor": valor,
                    "Estoque": 10
                }
                lista_prod.append(produto)
            except:
                print("O valor não corresponde a uma opção válida!")
        if (op == "L"):
            if len(lista_prod) == 0:
                print("Ta vazio menzinho")
            else:
                for indice, item in enumerate(lista_prod):
                    print(indice,item)
        if(op == "E"):
            try:
                remov = int(input("Coloca o ID que vc qr tirar da lista: "))
                del lista_prod[remov]
            except:
                print("O ID está incorreto")
        if(op=="S"):
            if len(lista_prod) < 5:
                print("pode sair não, 5 produtos")
                
            else:
                sair=True
                break
            
    cliente()

def cliente():
    op = ""
    while op != "S":
        print("O que você quer ? ")
        print("Comprar(C)\nVer Carrinho(V)\nSair(S)")
        op = input("Aguardando input: ")
        if op == "C":
            for indice, item in enumerate(lista_prod):
                    print(indice,item)
            try:
                id = int(input("Qual o id do produto ?"))
                lista_prod[id]["Estoque"] = lista_prod[id]["Estoque"] - 1
                found = False
                for item in lista_carrinho:
                    if lista_prod[id]["Descrição"] == item["Descrição"]:
                        item["Quantidade"] += 1
                        found = True
                if found == False:
                    produto_carrinho = {
                    "Descrição": lista_prod[id]["Descrição"],
                    "Valor": lista_prod[id]["Valor"],
                    "Quantidade": 1
                    }
                    lista_carrinho.append(produto_carrinho)
                print(lista_prod[id]["Estoque"])
            except:
                print("não")
        if op == "V":
            print(lista_carrinho)
            op_carrinho = input("quieres comprares?: ")
            if op_carrinho == "S":
                print("Voce comprou: ")
                print(lista_carrinho)
                lista_carrinho.clear()
            else:
                print("então ta bom")
        if op == "S":
            print("bye bye ")
            break



cadastrar()