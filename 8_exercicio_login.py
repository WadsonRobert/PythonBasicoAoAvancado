#Defina um usuário e senha e depois verifique se
#login do usuario é valido

USUARIO = 'wadson'
SENHA = '12345'


while True:
    login = input('Digite seu Usuario: ')
    senha = input('Digite sua senha: ')

    login = login.lower()
    senha = senha.lower()

    if login == USUARIO:
        if senha == SENHA:
            print('Sejá bem-vindo novamente')
            break
        else:
            print('Sua senha está incorreta')
    else:
        print('Usuario incorreto')
