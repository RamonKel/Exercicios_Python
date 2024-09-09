from time import sleep

print('-=' * 10)
print('IMPAR OU PAR?')
print('-=' * 10)

num = int(input('Digite um número e descubra se é IMPAR ou PAR: '))

verificador = num % 2

print('Analisando...')
sleep(2)

if verificador == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))

'''Realiza a verificação se um número é impar ou par, através do calculo
do módulo do número, se for 0 ele é par e 1 impar'''
