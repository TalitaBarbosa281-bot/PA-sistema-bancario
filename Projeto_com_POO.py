
class Cliente:
    def __init__(self, nome, cpf, salario, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario 
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def salario(self):
        return self.__salario
    @property
    def telefone(self):
        return self.__telefone

class Conta:
    def __init__(self, num_conta, tipo, cliente, saldo=0.0):
        self.__num_conta = num_conta
        self.__saldo = 0.0
        self.__tipo = tipo
        self.__cliente = cliente
        self.__transacoes = []

    @property
    def num_conta(self):
        return self.__num_conta
    @property
    def saldo(self):
        return self.__saldo 
    @property
    def tipo(self):
        return self.__tipo
    @property
    def cliente(self):
        return self.__cliente
    @property
    def transacoes(self):
        return self.__transacoes

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.transacoes.append(f"Depósito efetuado no valor de R$ {valor:.2f}")
            return True
        return False

    def sacar(self,valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque efetuado no valor de R$ {valor:.2f}")
            return True
        return False  

    def transferir(self, valor, conta_desejada):
        if self.sacar(valor):
            conta_desejada.depositar(valor)
            self.transacoes.append(f"Transferência realizada co  sucesso!")
            conta_desejada.transacoes.append(f"Tranferência recebida no valor de R$ {valor:.2f}")
            return True
        return False
            
class Agencia:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = numero
        self.__contas = []

    @property
    def nome(self):
        return self.__nome
    @property
    def numero(self):
        return self.__numero
    @property
    def contas(self):
        return self.__contas

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta.numero == numero:
                return conta
        return None
    def calcular_patrimonio(self):
        return sum(conta.saldo for conta in self.__contas)

    #Testes
agencia_nova = Agencia("Nova Agência", "001")
    #Criando os clientes
cliente1 = Cliente("Ana Beatriz", "123.456.789.00", 1600.0, "(79) 9888_1234")
cliente2 = Cliente("Pedro", "987.654.321.12", 2000.0, "(79) 9666-3333")
    #Criando as contas
conta1 = Conta("1000-2", "Corrente", cliente1, saldo=100.0)
conta2 = Conta("2000-4", "Poupança", cliente2, saldo= 1000.0)
    #Adicionando as contas na agencia
agencia_nova.adicionar_conta(conta1)
agencia_nova.adicionar_conta(conta2)
    #Testando as operações
print(f"Bem à {agencia_nova.nome} (Agência nº {agencia_nova.numero})")
print(f"Titular da conta 1: {conta1.cliente.nome}")
print(f"Saldo inicial da conta 1: R$ {conta1.saldo:.2f}")

conta1.depositar(300.0)
print(f"Saldo atualizado: R$: {conta1.saldo:.2f}")

conta1.sacar(100.0)
print(f"Saldo atualizado: R$ {conta1.saldo:.2f}")
    #Transferindo da conta 1 da conta 2
conta1.transferir(100.0, conta2)
print(f"Saldo da conta 1 atualizado: {conta1.saldo:.2f}")
print(f"Saldo da conta 2 atualizado: {conta2.saldo:.2f}")

    #Testando o patrimônio total
patrimonio = agencia_nova.calcular_patrimonio()
print(f"\nPatrimônio total da {agencia_nova.nome}: R$ {patrimonio:.2f}")

    #Exibindo o histórico de transações da conta 1
print("\nHistórico de transações da conta 1:")
for transacao in conta1.transacoes:
    print ("-", transacao)


   


