#Receba um número inteiro do usuário e mostre a tabuada desse número

num = int(input('Digite um número que deseje saber a tabuada: '))
valor = int(input('Digite até que número deseja saber a tabuda, (obs digite um número a mais): '))

rep = 0

while rep != valor:
    soma = num * rep
    print(f'{num} x {rep} = {soma}')
    rep += 1


