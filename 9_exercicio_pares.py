#Receba um número e mostre todo os números pares de 0 até o número digitado.

num1 = int(input('Digite um número inteiro e retornarei todos os pares até ele: '))

i = 1

while i <= num1:
    if i % 2 == 0:
        print(i)
    i += 1