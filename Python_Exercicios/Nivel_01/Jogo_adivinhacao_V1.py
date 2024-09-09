from random import choice

print('-=' * 30)
print('Irei pensar em um número de 0 a 5, consegue adivinhar qual?')
print('-=' * 30)

lista = [1,2,3,4,5]
sorteio = choice(lista)

num = int(input('Em que número eu pensei?: '))

if num == sorteio:
    print('Você adivinhou corretamente, parabens!')
else:
    print('Você errou, eu escolhi o número {}, não o {}'.format(sorteio,num))

'''O programa acima realiza um sorteio, e pede ao usuário para inserir um número
para realizar uma tentativa de acertar o número sorteado'''
