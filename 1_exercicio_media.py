#Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6)
#se ele ficou de recuperação (nota maior qou igual a 4) ou se ele foi
#reprovado (nota menor do que 4)

nota1b = float(input('Digite a nota do 1 bimestre: '))
nota2b = float(input('Digite a nota do 2 bimestre: '))
nota3b = float(input('Digite a nota do 3 bimestre: '))
nota4b = float(input('Digite a nota do 4 bimestre: '))

calculo = (nota1b + nota2b + nota3b + nota4b) / 4

if calculo >= 6:
    print('O aluno foi aprovado, ', calculo)
elif calculo >= 4:
    print('O aluno está de recuperação, ', calculo)
elif calculo < 4:
    print('O aluno foi reprovado, ', calculo)
else:
    print('Você não digitou um número valido')