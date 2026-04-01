import uuid

class Conta:
    def __init__(self,nome,saldo=0):
        self.id=str(uuid.uuid4())[:8]
        self.nome=nome
        self.saldo=saldo
        self.historico=[]

    def depositar(self,valor):
        if valor>0:self.saldo+=valor;self.historico.append("deposito "+str(valor));print("ok")
        else:print("erro")

    def sacar(self,valor):
        if valor<=self.saldo:self.saldo-=valor;self.historico.append("saque "+str(valor));print("foi")
        else:print("sem saldo")

class Banco:
    def __init__(self):
        self.contas={}

    def criar(self):
        n=input("nome:")
        c=Conta(n)
        self.contas[c.id]=c
        print("criado",c.id)

b=Banco()

while True:
    print("1 2 3 4 5 6 7")
    op=input()

    if op=="1":
        b.criar()

    elif op=="2":
        for c in b.contas.values():print(c.id,c.nome,c.saldo)

    elif op=="3":
        i=input("id:")
        v=float(input())
        if i in b.contas:b.contas[i].depositar(v)

    elif op=="4":
        i=input("id:")
        v=float(input())
        if i in b.contas:b.contas[i].sacar(v)

    elif op=="5":
        o=input();d=input();v=float(input())
        if o in b.contas and d in b.contas:
            if b.contas[o].saldo>=v:
                b.contas[o].saldo-=v
                b.contas[d].saldo+=v

    elif op=="6":
        i=input()
        if i in b.contas:
            for h in b.contas[i].historico:print(h)

    elif op=="7":
        break


