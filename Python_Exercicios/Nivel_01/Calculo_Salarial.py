print('-=' * 10)
print('CALCULO SALARIAL')
print('-=' * 10)

salario = float(input('Digite o seu salário: R$ '))

if salario > 1250:
    novo_salario = salario * 1.10
    print('Seu novo salário será de R$ {:.2f}'.format(novo_salario))
else:
    novo_salario1 = salario * 1.15
    print('Seu novo salário será de R$ {:.2f}'.format(novo_salario1))

'''O código acima realiza o calculo de um salário, dependendo da quantidade inserida
é realizado um aumento de 10 ou 15 porcento'''
