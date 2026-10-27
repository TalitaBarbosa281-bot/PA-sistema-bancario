class Conta:
    def __init__(self, num_conta):
        self.__num_conta = num_conta
        self.__saldo = 0.0

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def saldo(self):
        return self.__saldo 

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return

        self.__saldo += valor
        print("Depósito realizado com sucesso!")

    def sacar(self,valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return
        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return
        self.__saldo -= valor 
        print("Saque realizado com sucesso!")            
        
class Cliente:
    def __init__(self, nome, cpf, conta):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta = conta

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def conta(self):
        return self.__conta

    @property
    def num_conta(self):
        return self.__conta.num_conta

    @property
    def saldo(self):
        return self.__conta.saldo
    

class Banco:
    def __init__(self):
        self.__clientes = []
        self.__contas = []
        self.__prox_num_conta = 1

    def cadastrar_cliente(self, nome, cpf):
    # Gera o número da conta
         num_conta = self.__prox_num_conta
         self.__prox_num_conta += 1

    def listar_contas(self):
        if not self.__contas:
            print("Nenhuma conta encontrada.")
            return
        print("Lista de Contas Cadastradas")
        for cliente in self.__clientes:
            print(f"Titular: {cliente.nome}/nCPF: {cliente.cpf}/nNúmero da conta: {cliente.num_conta}")
    def procurar_conta(self, num_conta):
        for conta in self.__contas:
            if conta.num_conta == num_conta:
                return conta
        print(f"Conta não encontrada.")
        return None
    def consultar_saldo(self, num_conta):
        conta = self.procurar_conta(num_conta)
        if conta:
            print(f"O saldo da conta {conta.num_conta} é: R$ {conta.saldo:.2f}")
            return conta.saldo
        return None
        
            

    # Cria a conta
         conta = Conta(num_conta)

    # Cria o cliente associado à conta
         cliente = Cliente(nome, cpf, conta)

    # Armazena os objetos no banco
         self.__clientes.append(cliente)
         self.__contas.append(conta)
         return cliente
banco = Banco()

#testes
cliente1 = banco.cadastrar_cliente("Luiz", "12345678900")
cliente2 = banco.cadastrar_cliente("Talita", "987654321")


cliente1.conta.depositar(500)
print(cliente1.saldo)

banco.listar_contas()
banco.consultar_saldo(1)
conta_encontrada = banco.procurar_conta(2)
if conta_encontrada:
    conta_encontrada.depositar(50)
    
