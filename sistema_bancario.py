#etapa 1 
#Meu sistema bancario

conta_cliente = ""
saldo1 = 0.0
saldo2 = 0.0
#
#CADASTRO DE CLIENTE
#
def cadastrar_cliente():
    global conta_cliente # Para acessar e modificar variáveis de outra função foi declarada como global
    nome = input("Por favor, digite seu nome: ") 
    cpf = int(input("Por favor, digite o número de CPF: "))
    telefone = int(input("Por favor, digite telefone para contato: "))
    print(f"Parabéns {nome}, sua conta foi criada com sucesso. Você já pode aproveitar os outros benefícios.")
    conta_cliente = nome 
#
#CRIA CONTA CORRENTE OU POUPANÇA
#
def criar_conta():
    print("Digite o tipo de conta que deseja: ")
    print("[1] Criar conta corrente.")
    print("[2] Criar conta poupança.")
    num = int(input("Digite a operação que deseja realizar: "))
    if num == 1:
        global conta_corrente # Para acessar e modificar variáveis de outra função, foi declarada como global
        conta_corrente = 1.1
        global saldo1 # Para acessar e modificar variáveis de outra função, foi declarada como global
        saldo1 = 0.0
        print(f"Muito bem, o número da sua conta corrente é: {conta_corrente}")
    else:
        global conta_poupanca # Para acessar e modificar variáveis de outra função, foi declarada como global
        conta_poupanca = 1.2
        global saldo2 # Para acessar e modificar variáveis de outra função, foi declarada como global
        saldo2 = 0.0
        print(f"Muito bem, o número da sua conta poupança é: {conta_poupanca}")
#Ideia: gerar números aleatórios para as contas, e armazenar em uma lista, para que o
#cliente possa consultar o número da conta, além de seus dados pessoais.
#
#COSULTA DE SALDO
#
def consultar_saldo():
    print("Digite o nome do titular da conta: ")
    conta = input()
    if conta == conta_cliente:
        print("Digite o número da conta: ")
        num_conta = float(input())
        if num_conta == 1.1:
            print(f"Seu saldo é de: {saldo1} reais")
        else:
            print(f"O saldo é de: {saldo2} reais")
#
#DEPOSITO
#
def deposito():
    print("Digite o nome do titular da conta: ")
    conta = input()
    global saldo1, saldo2 # Para acessar e modificar variáveis de outra função foi declarada como global
    if conta == conta_cliente:
        print("Digite o número da conta: ")
        num_conta = float(input())
        if num_conta == 1.1:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo1 += valor_deposito
            print(f"Depósito realizado com sucesso! Seu novo saldo é de: {saldo1} reais")
        else:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo2 += valor_deposito
            print(f"Depósito realizado com sucesso! Seu novo saldo é de: {saldo2} reais")
def saque():
    print("Digite o nome do titular da conta: ")
    conta = input()
    global saldo1, saldo2 # Para acessar modificar variáveis de outra função foi declarada como global
    if conta == conta_cliente:
        print("Digite o número da conta: ")
        num_conta = float(input())
        if num_conta == 1.1:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            if valor_saque <= saldo1:
                saldo1 -= valor_saque
                print(f"Saque realizado com sucesso! Seu novo saldo é de: {saldo1} reais")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            if valor_saque <= saldo2:
                saldo2 -= valor_saque
                print(f"Saque realizado com sucesso! Seu novo saldo é de: {saldo2} reais")
            else:
                print("Saldo insuficiente para realizar o saque.")
while True:
 print("Olá, selecione abaixo a operação que deseja realizar: ")
 print("[1] Desejo me cadastrar")
 print("[2] criar uma conta")
 print("[3] consultar saldo")
 print("[4] Realizae depósito")
 print("[5] Realizar saque")
 print("[0] Sair do sistema")
 operacao = int(input("Digite o número da operação: "))

 if operacao == 1:
    cadastrar_cliente()
 elif operacao == 2:
    criar_conta()
 elif operacao == 3:
    consultar_saldo()
 elif operacao == 4:
    deposito()
 elif operacao == 5:
    saque()
 elif operacao == 0:
    print("Obrigado por utilizar nosso sistema bancário, até logo!")
    break
 else:
    print("Operação inválida, tente novamente.")

