import uuid

# =========================
# CLASSE CONTA
# =========================
class Conta:
    def __init__(self, nome, saldo=0):
        self.id = str(uuid.uuid4())[:8]
        self.nome = nome
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R${valor}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R${valor}")
            print("Saque realizado!")
        else:
            print("Saldo insuficiente.")

    def mostrar_dados(self):
        print("\n===== DADOS DA CONTA =====")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Saldo: R${self.saldo}")
        print("==========================")

    def mostrar_historico(self):
        print("\n===== HISTÓRICO =====")
        for h in self.historico:
            print(h)
        print("=====================")


# =========================
# CLASSE BANCO
# =========================
class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self):
        nome = input("Nome do cliente: ")
        conta = Conta(nome)
        self.contas[conta.id] = conta
        print(f"Conta criada! ID: {conta.id}")

    def buscar_conta(self, id):
        return self.contas.get(id)

    def listar_contas(self):
        print("\n=== CONTAS ===")
        for conta in self.contas.values():
            print(f"{conta.id} - {conta.nome} - R${conta.saldo}")
        print("==============")

    def transferir(self, origem_id, destino_id, valor):
        origem = self.buscar_conta(origem_id)
        destino = self.buscar_conta(destino_id)

        if origem and destino:
            if origem.saldo >= valor:
                origem.saldo -= valor
                destino.saldo += valor

                origem.historico.append(f"Transferência enviada: -R${valor}")
                destino.historico.append(f"Transferência recebida: +R${valor}")

                print("Transferência realizada!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta inválida.")


# =========================
# MENU PRINCIPAL
# =========================
banco = Banco()

while True:
    print("\n===== BANCO EMPRESARIAL =====")
    print("1 - Criar conta")
    print("2 - Listar contas")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Histórico")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        banco.criar_conta()

    elif opcao == "2":
        banco.listar_contas()

    elif opcao == "3":
        id = input("ID da conta: ")
        valor = float(input("Valor: "))
        conta = banco.buscar_conta(id)
        if conta:
            conta.depositar(valor)

    elif opcao == "4":
        id = input("ID da conta: ")
        valor = float(input("Valor: "))
        conta = banco.buscar_conta(id)
        if conta:
            conta.sacar(valor)

    elif opcao == "5":
        origem = input("Conta origem: ")
        destino = input("Conta destino: ")
        valor = float(input("Valor: "))
        banco.transferir(origem, destino, valor)

    elif opcao == "6":
        id = input("ID da conta: ")
        conta = banco.buscar_conta(id)
        if conta:
            conta.mostrar_historico()

    elif opcao == "7":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")


