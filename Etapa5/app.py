from abc import ABC, abstractmethod
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


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
      self.transacoes.append(
          f"Transferência enviada para {conta_desejada.num_conta}"
      )
      conta_desejada.transacoes.append(
          f"Transferência recebida de {self.num_conta}: + R$ {valor:.2f}"
      )
      return True
    return False

  @abstractmethod
  def tipo_conta(self):
    pass


class ContaCorrente(Conta):

  def __init__(self, num_conta, cliente, saldo=0.0, taxa_manutencao=15.0):
    super().__init__(num_conta, cliente, saldo)
    self.__taxa_manutencao = float(taxa_manutencao)

  @property
  def taxa_manutencao(self):
    return self.__taxa_manutencao

  def tipo_conta(self):
    return "Corrente"

  def descontar_taxa(self):
    if self.saldo >= self.__taxa_manutencao:
      super().sacar(self.__taxa_manutencao)
      self.transacoes.append(
          f"Taxa de manutenção descontada: - R$ {self.__taxa_manutencao:.2f}"
      )
      return True
    return False


class ContaPoupanca(Conta):

  def __init__(self, num_conta, cliente, saldo=0.0, taxa_rendimento=0.01):
    super().__init__(num_conta, cliente, saldo)
    self.__taxa_rendimento = float(taxa_rendimento)

  @property
  def taxa_rendimento(self):
    return self.__taxa_rendimento

  def tipo_conta(self):
    return "Poupança"

  def aplicar_rendimento(self):
    rendimento = self.saldo * self.__taxa_rendimento
    self.depositar(rendimento)
    self.transacoes.append(
        f"Rendimento aplicado (+{self.__taxa_rendimento*100}%): + R$"
        f" {rendimento:.2f}"
    )
    return True


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


# Instâncias iniciais
agencia_unica = Agencia("Agência Central UFS", "001")
c1 = Cliente("Ana Beatriz", "123.456.789-00", 1600.0, "(79) 98888-1234")
c2 = Cliente("Pedro", "987.654.321-12", 2000.0, "(79) 96666-3333")
agencia_unica.adicionar_conta(
    ContaCorrente("1000-2", c1, saldo=500.0, taxa_manutencao=10.0)
)
agencia_unica.adicionar_conta(
    ContaPoupanca("2000-4", c2, saldo=1000.0, taxa_rendimento=0.005)
)

mensagem_feedback = ""


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
        mensagem_feedback = f"Erro: Conta {num_conta} já existe."
      else:
        novo_cliente = Cliente(nome, cpf, salario, telefone)
        if tipo == "Corrente":
          nova_conta = ContaCorrente(num_conta, novo_cliente, saldo_inicial)
        else:
          nova_conta = ContaPoupanca(num_conta, novo_cliente, saldo_inicial)

        agencia_unica.adicionar_conta(nova_conta)
        mensagem_feedback = f"Conta {tipo} {num_conta} criada com sucesso!"

    elif acao == "operacao":
      num_origem = request.form.get("num_origem")
      tipo_op = request.form.get("tipo_op")
      valor = float(request.form.get("valor", 0))
      conta_origem = agencia_unica.buscar_conta(num_origem)

      if not conta_origem:
        mensagem_feedback = "Erro: Conta não encontrada."
      elif tipo_op == "depositar":
        conta_origem.depositar(valor)
        mensagem_feedback = f"Depósito de R$ {valor:.2f} realizado."
      elif tipo_op == "sacar":
        if not conta_origem.sacar(valor):
          mensagem_feedback = "Erro: Saldo insuficiente."
        else:
          mensagem_feedback = f"Saque de R$ {valor:.2f} realizado."
      elif tipo_op == "transferir":
        num_destino = request.form.get("num_destino")
        conta_destino = agencia_unica.buscar_conta(num_destino)
        if not conta_destino:
          mensagem_feedback = "Erro: Destino não encontrado."
        elif conta_origem.transferir(valor, conta_destino):
          mensagem_feedback = "Transferência realizada!"
        else:
          mensagem_feedback = "Erro na transferência."
      elif tipo_op == "taxa_manutencao":
        if isinstance(conta_origem, ContaCorrente):
          if conta_origem.descontar_taxa():
            mensagem_feedback = "Taxa de manutenção descontada com sucesso!"
          else:
            mensagem_feedback = "Erro: Saldo insuficiente para descontar taxa."
        else:
          mensagem_feedback = (
              "Erro: Esta operação é apenas para Conta Corrente."
          )
      elif tipo_op == "rendimento":
        if isinstance(conta_origem, ContaPoupanca):
          conta_origem.aplicar_rendimento()
          mensagem_feedback = "Rendimento aplicado com sucesso!"
        else:
          mensagem_feedback = "Erro: Esta operação é apenas para Conta Poupança."

    return redirect(url_for("index"))

  msg_atual = mensagem_feedback
  mensagem_feedback = ""
  return render_template(
      "index.html",
      agencia=agencia_unica,
      patrimonio=agencia_unica.calcular_patrimonio_total(),
      mensagem=msg_atual,
  )


if __name__ == "__main__":
  app.run(debug=True)
