valor1 = float(input('Insira um valor: '))
valor2 = float(input('Insira um segundo valor: '))
valor3 = float(input('Insira um terceiro valor: '))

lista = [valor1,valor2,valor3]

print('O maior valor é {:.1f} \n'
      'O menor valor é {:.1f}'.format(max(lista),min(lista)))

'''O código ao ser executado pede 3 valores numerais, logo após mostra seu maior e menor
valor'''
