# from datetime import date

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     # Um método de classe para criar
#     # Um objeto Pessoa através do ano de nascimento.
    
#     @classmethod
#     def apartirAnoNascimento(cls, nome, ano):
#         return cls(nome, date.today().year - ano)
    
#     # Método Estático : verificar se é maior de idade.
#     @staticmethod
#     def ehMaiorIdade(idade):
#         return idade >= 18

# pessoa1 = Pessoa('maria', 26)
# pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)

# print(pessoa1.idade)
# print(pessoa2.idade)

# # imprimir o resultado
# print(Pessoa.ehMaiorIdade(17))

class Conta:
    def __init__ (self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self, valor):
         self.saldo += valor
    def sacar(self, valor):
         self.saldo -= valor

pessoa1 = Conta(123, 3433, 'Wadson', 2500)

print(pessoa1.nomeTitular)

print(pessoa1.depositar(1000))

print(pessoa1.sacar(500))