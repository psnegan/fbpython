pizzas = {
    '1': {'nome': 'Mussarela', 'valor': 60.00},
    '2': {'nome': 'Calabresa', 'valor': 45.00},
    '3': {'nome': 'Frango Catupiry', 'valor': 70.00}
}

while True:
    print("Escolha uma opção:")
    print("1 - Comprar")
    print("2 - Sair")
    
    op = input("Digite a opção desejada: ")

    if op == '1':
        while True:
            print("Escolha o tipo de pizza:")
            for key, pizza in pizzas.items():
                print(f"{key} - {pizza['nome']} (R$ {pizza['valor']:.2f})")
            print("4 - Voltar")

            tipo = input("Digite o número do tipo de pizza desejada: ")

            if tipo in pizzas:
                pizza_escolhida = pizzas[tipo]
                print("-" * 20)
                print(f"Você escolheu {pizza_escolhida['nome']}")
                print(f"Valor: R$ {pizza_escolhida['valor']:.2f}")
                quantidade = int(input("Digite a quantidade desejada: "))
                total = pizza_escolhida['valor'] * quantidade
                print(f"Total a pagar: R$ {total:.2f}")
                break  # Volta ao menu principal após a compra
            elif tipo == '4':
                print("Voltando ao menu anterior...")
                break  # Volta ao menu principal
            else:
                print("Opção de pizza inválida. Tente novamente.")
    elif op == '2':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
