from math import trunc

N = float(input('Digite um número real(Ex: 1.25): '))
print('A porção inteira do número {}, é de {}'.format(N,trunc(N)))

#Verifica um valor do tipo float, após isso converte para sua porção inteira através da biblioteca math