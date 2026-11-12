from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- CLASSES DO SISTEMA BANCÁRIO (POO - ETAPA 5) ---
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
        self.__saldo = float(saldo)
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
            self.__saldo += valor
            self.transacoes.append(f"Depósito efetuado: + R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.transacoes.append(f"Saque efetuado: - R$ {valor:.2f}")
            return True
        return False  

    def transferir(self, valor, conta_desejada):
        if self.sacar(valor):
            conta_desejada.depositar(valor)
            self.transacoes.append(f"Transferência enviada para {conta_desejada.num_conta}")
            conta_desejada.transacoes.append(f"Transferência recebida de {self.num_conta}: + R$ {valor:.2f}")
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

    def calcular_patrimonio_total(self):
        return sum(conta.saldo for conta in self.__contas)


# --- INICIALIZAÇÃO DOS DADOS NA MEMÓRIA ---
agencia_unica = Agencia("Agência Central UFS", "001")

# Clientes e contas iniciais para demonstração na apresentação
c1 = Cliente("Ana Beatriz", "123.456.789-00", 1600.0, "(79) 98888-1234")
c2 = Cliente("Pedro", "987.654.321-12", 2000.0, "(79) 96666-3333")

agencia_unica.adicionar_conta(Conta("1000-2", "Corrente", c1, saldo=500.0))
agencia_unica.adicionar_conta(Conta("2000-4", "Poupança", c2, saldo=1000.0))

mensagem_feedback = ""


# --- ROTAS DO FLASK ---
@app.route("/", methods=["GET", "POST"])
def index():
    global mensagem_feedback
    
    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "criar_conta":
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            salario = float(request.form.get("salario", 0))
            telefone = request.form.get("telefone")
            num_conta = request.form.get("num_conta")
            tipo = request.form.get("tipo")
            saldo_inicial = float(request.form.get("saldo_inicial", 0))

            if agencia_unica.buscar_conta(num_conta):
                mensagem_feedback = f"Erro: Já existe uma conta com o número {num_conta}."
            else:
                novo_cliente = Cliente(nome, cpf, salario, telefone)
                nova_conta = Conta(num_conta, tipo, novo_cliente, saldo_inicial)
                agencia_unica.adicionar_conta(nova_conta)
                mensagem_feedback = f"Conta {num_conta} ({tipo}) criada para {nome}!"

        elif acao == "operacao":
            num_origem = request.form.get("num_origem")
            tipo_op = request.form.get("tipo_op")
            valor = float(request.form.get("valor", 0))
            conta_origem = agencia_unica.buscar_conta(num_origem)

            if not conta_origem:
                mensagem_feedback = "Erro: Conta de origem não encontrada."
            elif tipo_op == "depositar":
                if conta_origem.depositar(valor):
                    mensagem_feedback = f"Depósito de R$ {valor:.2f} realizado na conta {num_origem}."
                else:
                    mensagem_feedback = "Erro: Valor inválido para depósito."
            elif tipo_op == "sacar":
                if conta_origem.sacar(valor):
                    mensagem_feedback = f"Saque de R$ {valor:.2f} realizado na conta {num_origem}."
                else:
                    mensagem_feedback = "Erro: Saldo insuficiente ou valor inválido."
            elif tipo_op == "transferir":
                num_destino = request.form.get("num_destino")
                conta_destino = agencia_unica.buscar_conta(num_destino)
                if not conta_destino:
                    mensagem_feedback = "Erro: Conta de destino não encontrada."
                elif conta_origem.num_conta == conta_destino.num_conta:
                    mensagem_feedback = "Erro: Não é possível transferir para a mesma conta."
                elif conta_origem.transferir(valor, conta_destino):
                    mensagem_feedback = f"Transferência de R$ {valor:.2f} de {num_origem} para {num_destino} concluída!"
                else:
                    mensagem_feedback = "Erro: Saldo insuficiente para transferência."

        return redirect(url_for("index"))

    msg_atual = mensagem_feedback
    mensagem_feedback = ""  # Limpa a mensagem após exibir

    return render_template(
        "index.html",
        agencia=agencia_unica,
        patrimonio=agencia_unica.calcular_patrimonio_total(),
        mensagem=msg_atual
    )

if __name__ == "__main__":
    app.run(debug=True)
