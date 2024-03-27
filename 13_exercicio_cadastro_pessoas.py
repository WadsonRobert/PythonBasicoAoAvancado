#Faça um programa que o usuário possa cadastrar n pessoas,
#armazenando seu nome, idade e altura

lista_usuarios = []

print('===== Cadastro de Usuários =====')

while True:
    sair = input('Caso deseje sair digite SAIR, continuar pressione qualquer tecla: ')
    sair = sair.lower()
    print('')
    
    if sair == 'sair':
        print('Cadastro encerrado')
        break
    else:
        nome = input('Digite o nome do usuário que deseja cadastrar: ')
        idade = int(input('Digite a idade do usuário que deseja cadastra: '))
        altura = int(input('Digite a altura em cm do usuario que deseja cadastrar: '))

        usuarios = {'nome': nome, 'idade': idade, 'altura': altura}
        lista_usuarios.append(usuarios)



print(lista_usuarios)


    
