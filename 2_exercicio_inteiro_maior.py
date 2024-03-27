#Receba 3 número inteiros e exiba o maior deles

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n3:
    print(f'O {n1} foi o maior numero digitado')
elif n2 > n1 and n3:
    print(f'O {n2} foi o maior número digitado')
else:
    print(f'O {n3} foi o maior número digitado')
    