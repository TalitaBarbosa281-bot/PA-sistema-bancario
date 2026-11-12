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
        self.__tipo = tipo         
        self.__cliente = cliente    # Objeto Cliente
        self.__saldo = saldo
        self.__transacoes = []      # Histórico de transações

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def tipo(self):
        return self.__tipo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @property
    def transacoes(self):
        return self.__transacoes

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: +R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__transacoes.append(f"Saque: -R$ {valor:.2f}")
            return True
        return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self.__transacoes.append(f"Transferência enviada: -R$ {valor:.2f} para a conta {conta_destino.num_conta}")
            conta_destino.transacoes.append(f"Transferência recebida: +R$ {valor:.2f} da conta {self.__num_conta}")
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
            if conta.num_conta == numero:
                return conta
        return None

    def calcular_patrimonio(self):
        return sum(conta.saldo for conta in self.__contas)


#testes

if __name__ == "__main__":
    # 1. Criando a Agência de forma genérica
    minha_agencia = Agencia("Agência Central", "001")

    # 2. Criando Clientes
    cliente1 = Cliente("Ana Silva", "123.456.789-00", 3500.0, "(79) 99999-1111")
    cliente2 = Cliente("Carlos Souza", "987.654.321-11", 4200.0, "(79) 98888-2222")

    # 3. Criando Contas associadas aos Clientes
    conta1 = Conta("1001-5", "Corrente", cliente1, saldo=500.0)
    conta2 = Conta("1002-3", "Poupança", cliente2, saldo=1200.0)

    # 4. Adicionando as contas à Agência[cite: 1]
    minha_agencia.adicionar_conta(conta1)
    minha_agencia.adicionar_conta(conta2)

    # 5. Testando operações
    print(f"--- Bem-vindo à {minha_agencia.nome} (Agência nº {minha_agencia.numero}) ---")
    print(f"Titular da conta 1: {conta1.cliente.nome}")
    print(f"Saldo inicial da conta 1: R$ {conta1.saldo:.2f}")

    conta1.depositar(300.0)
    print(f"Saldo após depósito: R$ {conta1.saldo:.2f}")

    conta1.sacar(100.0)
    print(f"Saldo após saque: R$ {conta1.saldo:.2f}")

    # Transferindo da conta 1 para a conta 2
    conta1.transferir(100.0, conta2)
    print(f"Saldo da conta 1 após transferência: R$ {conta1.saldo:.2f}")
    print(f"Saldo da conta 2 após receber transferência: R$ {conta2.saldo:.2f}")

    # 6. Testando o patrimônio total da agência
    patrimonio = minha_agencia.calcular_patrimonio()
    print(f"\nPatrimônio total da {minha_agencia.nome}: R$ {patrimonio:.2f}")

    # 7. Exibindo o histórico de transações da conta 1
    print("\nHistórico de transações da Conta 1:")
    for transacao in conta1.transacoes:
        print("-", transacao)
