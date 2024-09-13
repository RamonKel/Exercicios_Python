print('-=' * 10)
print('COMPARANDO NÚMEROS')
print('-=' * 10)

num1 = int(input('Insira um valor inteiro: '))
num2 = int(input('Insira outro valor inteiro: '))

if num1 > num2:
    print('O primeiro valor é MAIOR!')
elif num2 > num1:
    print('O segundo valor é MAIOR!')
elif num1 == num2:
    print('Os dois são IGUAIS!')
