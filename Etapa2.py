print('Olá como deseja proseguir:\n [1] Criar conta\n [2] Fazer cadastro\n [3] Encotrar conta \n [4] Consultar saldo\n [5] Depositar\n [6] Sacar')
operacao = input("Digite o número correspondente a operação: ")
clientes = []
contas = []

def fazerCadastro(clientes):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        clientes.append([cpf, nome])
        print ("Cadastro realizado com sucesso!")

def criarConta(clientes, contas):
    nome = input("Digite o nome do titular: ")
    cpf = input("Digite seu CPF: ")

    numConta = str(len(contas) + 1)
    contas.append([numConta, cpf, 0.0])
    print(f"Conta de número {numConta} criada com sucesso!")

def listarContas(contas, clientes):
        if not contas:
               print("Nenhuma conta encontrada.")
               return
        for conta in contas:    
           for cliente in clientes:
               if cliente[0] == conta[1]:
                      nome = cliente[1]
                      break
           print(f"Conta: {conta[0]}\n Titular: {nome}\n {conta[1]}\n Saldo: R$ {conta[2]:.2f}\n")
                      
