from random import shuffle

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quanto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
ordem = shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

#Realiza o embaralhamento da lista inserida com a função shuffle