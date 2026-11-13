from abc import ABC, abstractmethod

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

#CLASSE ABSTRATA CONTA (Superclasse)
class Conta(ABC):
    def __init__(self, num_conta, cliente, saldo=0.0):
        self.__num_conta = num_conta
        self.__saldo = float(saldo)
        self.__cliente = cliente  
        self.__transacoes = []

    @property
    def num_conta(self):
        return self.__num_conta

    @property   
    def saldo(self):
        return self.__saldo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def transacoes(self):
        return self.__transacoes

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: + R$ {valor:.2f}")
            return True
        return False     

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__transacoes.append(f"Saque: - R$ {valor:.2f}")
            return True
        return False

    def transferir(self, valor, conta_desejada):
        if self.sacar(valor):
            conta_desejada.depositar(valor)
            self.__transacoes.append(f"Transferência enviada para Conta {conta_desejada.num_conta}")
            conta_desejada.__transacoes.append(f"Transferência recebida da Conta {self.__num_conta}: + R$ {valor:.2f}")
            return True
        return False

    #Método abstrato: obriga as classes filhas a implementarem
    @abstractmethod
    def tipo_conta(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, num_conta, cliente, saldo=0.0, taxa_manutencao=15.0):
        super().__init__(num_conta, cliente, saldo)
        self.__taxa_manutencao = float(taxa_manutencao)

    def tipo_conta(self):
        return "Corrente"

    def descontar_taxa(self):
        if self.saldo >= self.__taxa_manutencao:
            super().sacar(self.__taxa_manutencao)
            self.transacoes.append(f"Taxa de manutenção descontada: - R$ {self.__taxa_manutencao:.2f}")
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, num_conta, cliente, saldo=0.0, taxa_rendimento=0.01):
        super().__init__(num_conta, cliente, saldo)
        self.__taxa_rendimento = float(taxa_rendimento)

    def tipo_conta(self):
        return "Poupança"

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.__taxa_rendimento
        self.depositar(rendimento)
        self.transacoes.append(f"Rendimento aplicado: + R$ {rendimento:.2f}")
        return True

class Agencia:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = numero
        self.__contas = [] 

    @property
    def nome(self):
        return self.__nome

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta.num_conta == numero:
                return conta
        return None

    def calcular_patrimonio_total(self):
        return sum(conta.saldo for conta in self.__contas)

#TESTES
if __name__ == "__main__":
    #Criando a Agência
    agencia = Agencia("Agência Central", "001")

    #Criando Clientes
    cli1 = Cliente("Ana Beatriz", "123.456.789-00", 1600.0, "(79) 98888-1234")
    cli2 = Cliente("Pedro", "987.654.321-12", 2000.0, "(79) 96666-3333")

    #Criando Contas (Corrente e Poupança herdando de Conta)
    conta1 = ContaCorrente("1001-X", cli1, saldo=600.0)
    conta2 = ContaPoupanca("2002-Y", cli2, saldo=1000.0)

    #Adicionando na Agência
    agencia.adicionar_conta(conta1)
    agencia.adicionar_conta(conta2)

    print(f"--- Bem-vindo à {agencia.nome} ---")
    print(f"Patrimônio Inicial da Agência: R$ {agencia.calcular_patrimonio_total():.2f}\n")

    #Realizando Operações
    print("Realizando depósito na Conta 1...")
    conta1.depositar(200.0)

    print("Realizando transferência da Conta 2 para a Conta 1...")
    conta2.transferir(300.0, conta1)

    print("Aplicando rendimento na Conta Poupança 2...")
    conta2.aplicar_rendimento()

    print("Descontando taxa de manutenção na Conta Corrente 1...")
    conta1.descontar_taxa()

    #Resultados 
    print("\n================ EXTRATOS FINAIS ================")
    for conta in [conta1, conta2]:
        print(f"\nConta: {conta.num_conta} ({conta.tipo_conta()})")
        print(f"Titular: {conta.cliente.nome}")
        print(f"Saldo Atual: R$ {conta.saldo:.2f}")
        print("Histórico de Transações:")
        for t in conta.transacoes:
            print(f"  - {t}")

    print(f"\nPatrimônio Final da Agência: R$ {agencia.calcular_patrimonio_total():.2f}")

