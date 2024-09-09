print('-=' * 12)
print('ANALISE DE UM TRIANGULO')
print('-=' * 12)

ab = float(input('Insira o valor do primeiro segmento: '))
cd = float(input('Insira o valor do segundo segmento: '))
ef = float(input('Insira o valor do terceiro segmento: '))

if ab+cd>ef and cd+ef>ab and ab+ef>cd:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo..')