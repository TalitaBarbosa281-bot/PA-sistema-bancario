#etapa 1 
#Meu sistema bancario

print("Olá, selecione abaixo a operação que deseja realizar: ")
print("[1] Desejo me cadastrar")
print("[2] criar uma conta")
print("[3] consultar saldo")
print("[4] Realizae depósito")
print("[5] Realizar saque")

conta_cliente = ""
saldo1 = 0.0
saldo2 = 0.0

print("Digite o número da operação:")
operacao = int(input())

def cadastrar_cliente():
    nome = input("Por favor, digite seu nome: ") 
    cpf = int(input("Por favor, digite o número de CPF: "))
    telefone = int(input("Por favor, digite telefone para contato: "))
    print("Parabéns {nome}, sua conta foi criada com sucesso. Você já pode aproveitar os outros benefícios.")
    conta_cliente = nome 
def criar_conta():
    print("Digite o tipo de conta que deseja: ")
    print("[1] Criar conta corrente.")
    print("[2] Criar conta poupança.")
    num = int(input("Digite a operação que deseja realizar: "))
    if num == 1:
        conta_corrente = 1.1
        saldo1 = 0.0
        print("Muito bem, o número da sua conta corrente é: {conta_corrente}")
    else:
        conta_poupanca = 1.2
        saldo2 = 0.0
        print("Muito bem, o número da sua conta corrente é: {conta_corrente}")

def consultar_saldo():
    print("Digite o nome do titular da conta: ")
    conta = int(input())
    if conta == conta_cliente:
        print("Digite o número da conta: ")
        num_conta = int(input())
        if num_conta == 1.1:
            print(f"Seu saldo é de: {saldo1} reais")
        else:
            print(f"O saldo é de: {saldo2} reais")


