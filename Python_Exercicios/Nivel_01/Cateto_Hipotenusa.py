from math import sqrt, pow

Cateto1 = float(input('Digite o valor do primeiro cateto: '))
Cateto2 = float(input('Digite o valor do segundo cateto: '))
Raiz = pow(Cateto1,2) + pow(Cateto2,2)
Hipotenusa = sqrt(Raiz)

print('A hipotenusa dos catetos é {}'.format(Hipotenusa))

#Atribui 2 valores para os catetos, logo após realiza a operação da raiz, dando a resultado da hipotenusa