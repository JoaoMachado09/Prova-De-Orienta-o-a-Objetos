class ContaCorrente():
    def __init__(self):
        self.NumeroConta = 0
        self.nome = ''
        self.saldo = 0
    
    def setSaldo(self, valor):
        if valor < 0:
            print("Erro: saldo negativo")
        else:
            self.saldo = valor
    
    def getSaldo(self):
        return self.saldo
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setNumeroConta(self, NumeroConta):
        self.NumeroConta = NumeroConta

    def __str__(self):
        return f"Nome: {self.nome}, Número da Conta: {self.NumeroConta}, Saldo: {self.saldo}"


class ContaComum(ContaCorrente):
    def __init__(self):
        ContaCorrente.__init__(self)
    
    def depositar(self, valor):
        if valor >= 100:
            NovoSaldo = self.getSaldo() + valor
        else:
            NovoSaldo = self.getSaldo() + (valor * 0.99)
    
        self.setSaldo(NovoSaldo)
    
    def sacar(self, valor):
        total = valor + 2.5
        if self.getSaldo() >= total:
            self.setSaldo(self.getSaldo() - total)
            return True
        else:
            print('Saldo insuficiente para saque')
            return False


class ContaEspecial(ContaCorrente):
    def __init__(self):
        ContaCorrente.__init__(self)
        self.saques_realizados = 0
    
    def depositar(self, valor): 
        self.setSaldo(self.getSaldo() + valor)  
    
    def sacar(self, valor):
        taxa = 0
        if self.saques_realizados >= 3:
            taxa = 5.00
        total = valor + taxa
        if self.getSaldo() >= total:
            self.setSaldo(self.getSaldo() - total)
            self.saques_realizados += 1
            return True
        else:
            print("Saldo insuficiente para saque")
            return False
        
    def resetar_saques(self):
        self.saques_realizados = 0


# Teste do código
conta1 = ContaComum()
conta1.setNome("João")
conta1.setSaldo(100)
conta1.setNumeroConta(190)

# Operações na conta1
conta1.depositar(50)  # Deposita 50 na conta comum
conta1.sacar(30)  # Tenta sacar 30 da conta comum

print(conta1)  # Imprime o estado da conta1 após operações

conta2 = ContaEspecial()
conta2.setSaldo(200)
conta2.setNome("Maria")
conta2.setNumeroConta(120)

# Operações na conta2
conta2.depositar(100)  # Deposita 100 na conta especial
conta2.sacar(50)  # Tenta sacar 50 da conta especial
conta2.sacar(60)  # Tenta sacar 60 da conta especial
conta2.sacar(70)  # Tenta sacar 70 da conta especial (a partir daqui vai ter a taxa de saque)

print(conta2)  # Imprime o estado da conta2 após operações
