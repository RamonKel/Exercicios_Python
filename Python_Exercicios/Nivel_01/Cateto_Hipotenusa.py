from math import sqrt, pow, hypot

cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
raiz = pow(cateto1,2) + pow(cateto2,2)
hipotenusa = sqrt(raiz)

print('A hipotenusa dos catetos é {:.2f}'.format(hipotenusa))

#Atribui 2 valores para os catetos, logo após realiza a operação da raiz, dando a resultado da hipotenusa