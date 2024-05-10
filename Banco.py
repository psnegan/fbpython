

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def abrir_conta(self, tipo):
        tipo = tipo.lower()  # Converte o tipo de conta para letras minúsculas
        if tipo == "poupanca":
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            dia_conta = int(input("Digite o dia de conta da poupança: "))
            self.contas.append(Poupanca(numero, saldo, dia_conta))
            print("Conta poupança aberta com sucesso.")
        elif tipo == "corrente":
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            limite = float(input("Digite o limite da conta corrente: "))
            self.contas.append(Corrente(numero, saldo, limite))
            print("Conta corrente aberta com sucesso.")
        elif tipo == "empresarial":
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            limite = float(input("Digite o limite da conta empresarial: "))
            cnpj = input("Digite o CNPJ da conta empresarial: ")
            self.contas.append(Empresarial(numero, saldo, limite, cnpj))
            print("Conta empresarial aberta com sucesso.")
        elif tipo == "estudantil":
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            limite = float(input("Digite o limite da conta estudantil: "))
            instituicao = input("Digite a instituição da conta estudantil: ")
            self.contas.append(Estudantil(numero, saldo, limite, instituicao))
            print("Conta estudantil aberta com sucesso.")
        else:
            print("Tipo de conta não suportado.")

    def fechar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                print(f"Conta {numero} fechada com sucesso.")
                return
        print("Conta não encontrada.")

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

    def realizar_movimento(self, numero_conta, tipo_movimento, valor):
        for conta in self.contas:
            if conta.numero == numero_conta:
                if tipo_movimento == "saque":
                    if conta.saldo >= valor:
                        conta.sacar(valor)
                    else:
                        if isinstance(conta, Corrente) and valor <= conta.limite:
                            print("Saldo insuficiente. Utilizando o limite da conta corrente.")
                            conta.saldo -= valor
                            conta.limite -= valor
                        else:
                            print("Saldo insuficiente e limite atingido.")
                elif tipo_movimento == "deposito":
                    conta.depositar(valor)
                # Verificar se é aniversário da conta e atualizar saldo
                if isinstance(conta, Poupanca) and valor > 0 and conta.dia_conta == 10:
                    conta.saldo = (conta.saldo * 0.0005) + conta.saldo
                return
        print("Conta não encontrada.")

    def solicitar_cheque(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta and isinstance(conta, Corrente):
                if conta.saldo >= 30:
                    conta.sacar(30)
                    print("Cheque solicitado com sucesso.")
                else:
                    print("Saldo insuficiente para solicitar cheque.")
                return
        print("Conta não encontrada ou não é conta corrente.")

    def solicitar_emprestimo(self, numero_conta, valor):
        for conta in self.contas:
            if conta.numero == numero_conta:
                if isinstance(conta, Empresarial) and valor <= 10000:
                    conta.depositar(valor)
                    print("Empréstimo aprovado.")
                elif isinstance(conta, Estudantil) and valor <= 5000:
                    conta.depositar(valor)
                    print("Empréstimo aprovado.")
                else:
                    print("Empréstimo não aprovado.")
                return
        print("Conta não encontrada.")
        

# Exemplo de uso:
banco = Banco("Meu Banco")

tipo_conta = input("Digite o tipo de conta que deseja abrir (poupanca, corrente, empresarial ou estudantil): ")

banco.abrir_conta(tipo_conta)

banco.listar_contas()

banco.fechar_conta(input("Digite o número da conta que deseja fechar: "))

banco.listar_contas()
