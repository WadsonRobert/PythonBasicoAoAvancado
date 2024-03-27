class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf= cpf

    def logar_sistema(self):
        print(f'{self.nome}, está logando no sistema...')



p1 = Pessoas('Wadson', 20, '07399246130')
p2 = Pessoas('Ana', 18, '0492388434')

p1.logar_sistema()
p2.logar_sistema()