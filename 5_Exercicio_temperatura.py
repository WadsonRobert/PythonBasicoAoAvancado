#Receba uma temperatura em farenheit e exiba em graus celsius.
# c= 5 * f - 32/9

temp_f = float(input('Digite uma temperatura em graus farenheit: '))

temperatura_celsius = 5 * ((temp_f -32) / 9)

print(f'A temperatura em Graus Celsius é de {temperatura_celsius:.2f} C')
