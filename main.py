import uuid

class ContaCliente:
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
        self.ContaCliente={}

    def criar(self):
        n=input("nome:")
        c=ContaCliente(n)
        self.ContaCliente[c.id]=c
        print("criado",c.id)

b=Banco()

while True:
    print("1 2 3 4 5 6 7")
    op=input()

    if op=="1":
        b.criar()

    elif op=="2":
        for c in b.ContaCliente.values():print(c.id,c.nome,c.saldo)

    elif op=="3":
        i=input("id:")
        v=float(input())
        if i in b.ContaCliente:b.ContaCliente[i].depositar(v)

    elif op=="4":

        i=input("id:")
        v=float(input())
        if i in b.ContaCliente:b.ContaCliente[i].sacar(v)

    elif op=="5":
        o=input();d=input();v=float(input())
        if o in b.ContaCliente and d in b.ContaCliente:
            if b.ContaCliente[o].saldo>=v:
                b.ContaCliente[o].saldo-=v
                b.ContaCliente[d].saldo+=v

    elif op=="6":
        i=input()
        if i in b.ContaCliente:
            for h in b.ContaCliente[i].historico:print(h)

    elif op=="7":
        break
    else:
        print ('erro')