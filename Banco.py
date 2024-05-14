from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def __str__(self):
        return f"Conta ({self.numero}) - Saldo: R${self.saldo:.2f}"

class Poupanca(Conta):
    def __init__(self, numero, saldo, dia_conta):
        super().__init__(numero, saldo)
        self.dia_conta = dia_conta

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def __str__(self):
        return f"Poupança ({self.numero}) - Saldo: R${self.saldo:.2f} - Dia da Conta: {self.dia_conta}"

class Corrente(Conta):
    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif self.saldo + self.limite >= valor:
            self.limite -= (valor - self.saldo)
            self.saldo = 0
            print(f"Saque de R${valor:.2f} realizado com sucesso utilizando o limite da conta corrente.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def __str__(self):
        return f"Corrente ({self.numero}) - Saldo: R${self.saldo:.2f} - Limite: R${self.limite:.2f}"

class EmprestimoEmpresa(Conta):
    def __init__(self, numero, saldo, valor_emprestimo):
        super().__init__(numero, saldo)
        self.valor_emprestimo = valor_emprestimo

    def pedir_emprestimo(self, valor):
        if self.valor_emprestimo >= valor:
            self.saldo += valor
            self.valor_emprestimo -= valor
            print(f"Empréstimo de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de empréstimo indisponível.")

    def sacar(self, valor):
        print("Operação de saque não disponível para conta de empréstimo empresarial.")

    def depositar(self, valor):
        print("Operação de depósito não disponível para conta de empréstimo empresarial.")

    def __str__(self):
        return f"EmprestimoEmpresa ({self.numero}) - Saldo: R${self.saldo:.2f} - Empréstimo Disponível: R${self.valor_emprestimo:.2f}"

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def abrir_conta(self):
        tipo_conta = input("Digite o tipo de conta (poupanca, corrente, emprestimoEmpresa): ").strip().lower()
        numero = input("Digite o número da conta: ").strip()
        saldo = float(input("Digite o saldo inicial: "))

        if tipo_conta == "poupanca":
            dia_conta = int(input("Digite o dia da conta poupança: "))
            conta = Poupanca(numero, saldo, dia_conta)
        elif tipo_conta == "corrente":
            limite = float(input("Digite o limite da conta corrente: "))
            conta = Corrente(numero, saldo, limite)
        elif tipo_conta == "emprestimoEmpresa":
            valor_emprestimo = float(input("Digite o valor do empréstimo disponível: "))
            conta = EmprestimoEmpresa(numero, saldo, valor_emprestimo)
        else:
            print("Tipo de conta inválido.")
            return

        self.contas.append(conta)
        print("Conta aberta com sucesso.")

    def fechar_conta(self):
        numero_conta = input("Digite o número da conta a ser fechada: ").strip()
        for conta in self.contas:
            if conta.numero == numero_conta:
                self.contas.remove(conta)
                print("Conta fechada com sucesso.")
                return
        print("Conta não encontrada.")

    def listar_contas(self):
        print(f"Contas no {self.nome}:")
        for conta in self.contas:
            print(conta)

    def operar_conta(self):
        numero_conta = input("Digite o número da conta: ").strip()
        conta = next((c for c in self.contas if c.numero == numero_conta), None)
        if not conta:
            print("Conta não encontrada.")
            return

        operacao = input("Digite a operação (sacar, depositar, pedir_emprestimo): ").strip().lower()
        if operacao == "sacar":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif operacao == "depositar":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif operacao == "pedir_emprestimo" and isinstance(conta, EmprestimoEmpresa):
            valor = float(input("Digite o valor do empréstimo: "))
            conta.pedir_emprestimo(valor)
        else:
            print("Operação inválida ou não disponível para este tipo de conta.")

# Exemplo de uso interativo:
banco = Banco("Meu Banco")

while True:
    print("\nMenu:")
    print("1. Abrir conta")
    print("2. Fechar conta")
    print("3. Listar contas")
    print("4. Operar em uma conta")
    print("5. Sair")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        banco.abrir_conta()
    elif escolha == "2":
        banco.fechar_conta()
    elif escolha == "3":
        banco.listar_contas()
    elif escolha == "4":
        banco.operar_conta()
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
