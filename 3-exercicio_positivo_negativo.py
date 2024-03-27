#Receba um Número e exiba se ele é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero < 0:
    print('O número digitado é negativo: ', numero)
elif numero > 0:
    print('O número digitado é positivo: ', numero)
else:
    print('O Numero digitado é 0')
