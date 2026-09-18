clientes = {}
contas = {}

numeros_conta = set()
cpfs = set()

def fazerCadastro(clientes):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        if cpf in cpfs:
            print("CPF já cadastrado.")
            return
        cpfs.add(cpf)
        clientes[cpf] = nome
        print ("Cadastro realizado com sucesso!")

def criarConta(clientes, contas):
    cpf = input("Digite o CPF do titular: ")
    if cpf not in clientes:
        print("CPF não cadastrado. Por favor, faça o cadastro primeiro.")
        return

    numConta = str(len(numeros_conta) + 1)
    numeros_conta.add(numConta)
    contas[numConta] = {"cpf": cpf, "saldo": 0.0}
    print(f"Conta de número {numConta} criada com sucesso!")

def listarContas(contas, clientes):
        if not contas:
               print("Nenhuma conta encontrada.")
               return
        print("\n--- CONTAS CADASTRADAS ---")

        for numConta, conta in contas.items():
            cpf = conta["cpf"]
            nome = clientes.get(cpf, "Nome não encontrado")
            saldo = conta["saldo"]
            print(f"Conta: {numConta}, Titular: {nome}, CPF: {cpf}, Saldo: {saldo}")
def depositar(contas):
    numConta = input("Digite o número da conta: ")
    if numConta not in contas:
        print("Conta não encontrada.")
        return
    valor = float(input("Digite o valor a ser depositado: "))
    contas[numConta]["saldo"] += valor
    print(f"Depósito de {valor} realizado com sucesso! Novo saldo: {contas[numConta]['saldo']}")

def sacar(contas):
    numConta = input("Digite o número da conta: ")
    if numConta not in contas:
        print("Conta não encontrada.")
        return
    valor = float(input("Digite o valor a ser sacado: "))
    if contas[numConta]["saldo"] < valor:
        print("Saldo insuficiente.")
        return
    contas[numConta]["saldo"] -= valor
    print(f"Saque de {valor} realizado com sucesso! Novo saldo: {contas[numConta]['saldo']}")
def consultarConta(contas, clientes):
    numConta = input("Digite o número da conta: ")
    if numConta not in contas:
        print("Conta não encontrada.")
        return
    cpf = contas[numConta]["cpf"]
    nome = clientes.get(cpf, "Nome não encontrado")
    saldo = contas[numConta]["saldo"]
    print(f"Titular: {nome}, CPF: {cpf}, Saldo: {saldo}")
def consultarSaldo(contas, clientes):
    numConta = input("Digite o número da conta: ")
    if numConta not in contas:
        print("Conta não encontrada.")
        return
    saldo = contas[numConta]["saldo"]
    print(f"Saldo da conta {numConta}: {saldo}")

while True: 
    print("\nOlá! Como deseja prosseguir?\n[1] Fazer cadastro \n[2] Criar conta \n[3] Encontrar conta\n[4] Consultar saldo\n[5] Depositar\n[6] Sacar\n[7] Listar contas\n[0] Sair do sistema") 
    operacao = input("Digite o número correspondente à operação: ") 
    if operacao == "1": 
        fazerCadastro(clientes)
    elif operacao == "2": 
        criarConta(clientes, contas)
    elif operacao == "3": 
        consultarConta(contas, clientes) 
    elif operacao == "4": 
        consultarSaldo(contas, clientes) 
    elif operacao == "5": 
        depositar(contas) 
    elif operacao == "6": 
        sacar(contas) 
    elif operacao == "7": 
        listarContas(contas, clientes)
    elif operacao == "0": 
        print("Sistema encerrado.") 
        break 
    else: 
        print("Operação inválida.")
