from random import choice
from time import sleep

print('Vamos jogar? \n'
      'Você consegue me vencer no pedra,papel,tesoura?')
print('Suas opções: \n'
      '[ 1 ] Pedra \n'
      '[ 2 ] Papel \n'
      '[ 3 ] Tesoura ')
escolha = int(input('Digite a opção que deseja jogar: '))
lista = [1,2,3]
sorteio = choice(lista)
if escolha != lista:
      print('Opção invalida, escolha novamente!')

sleep(1)
print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)

if escolha == sorteio:
      print('Empate, vamos novamente!')
elif sorteio == 1 and escolha == 2:
      print('-'*30)
      print('Você venceu, eu escolhi Pedra..')
      print('-' * 30)
elif sorteio == 2 and escolha == 3:
      print('-'*30)
      print('Você venceu, eu escolhi Papel..')
      print('-' * 30)
elif sorteio == 3 and escolha == 1:
      print('-'*30)
      print('Você venceu, eu escolhi Tesoura..')
      print('-' * 30)
elif sorteio == 2 and escolha == 1:
      print('-'*30)
      print('Eu venci, eu escolhi Papel!')
      print('-' * 30)
elif sorteio == 1 and escolha == 3:
      print('-'*30)
      print('Eu venci, eu escolhi Pedra!')
      print('-' * 30)
elif sorteio == 3 and escolha == 2:
      print('-'*30)
      print('Eu venci, eu escolhi Tesoura!')
      print('-' * 30)
