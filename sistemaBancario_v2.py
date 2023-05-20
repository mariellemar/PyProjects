from abc import ABC, abstractclassmethod, abstractproperty, abstractstaticmethod
from datetime import datetime

#Cliente
class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

#Conta
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"  
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True
    
class ContaCorrente(Conta):
    def  __init__(self, numero, cliente, limite_saques = 3, limite = 500):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saques
    
    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self.historico.transacao if transacao ["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saque >= self.limite_saque
        
        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)
        return False
    def __str__(self) -> str:
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
    """
        
#Historico
class Historico:
    def __init__(self, transacao):
        self._transacao = []
        
    @property
    def transacao(self):
        return self._transacao
    
    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-&Y %H:%M:%s"),
            }
        )
        
#Transacao
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass
#Saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
#Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            