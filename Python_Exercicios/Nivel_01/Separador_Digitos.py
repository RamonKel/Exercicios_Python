numero = int(input('Digite um número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

'''O calculo acima verifica a posição do numero em sua ordem, realizando
uma divisão inteira, e logo após o seu módulo, que resulta na resposta'''

print('Analisando o número {}...'.format(numero))
print('A unidade é {} \n'
      'A dezena é {} \n'
      'A centena é {} \n'
      'O milhar é {} '.format(unidade,dezena,centena,milhar))