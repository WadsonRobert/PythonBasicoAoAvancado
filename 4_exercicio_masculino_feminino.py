#Receba F para feminino e M para masculino e exiba o sexo da pessoa

sexo = input('Digite ( F ) para feminino e ( M ) para masculino')

sexo = sexo.lower()

if sexo == 'f':
    print('Seu sexo é feminino')
elif sexo == 'm':
    print('Seu sexo é Masculino')
else:
    print('Você digitou valor inválido')