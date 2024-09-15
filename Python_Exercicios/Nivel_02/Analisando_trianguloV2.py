print('-=' * 12)
print('ANALISE DE UM TRIANGULO')
print('-=' * 12)

ab = float(input('Insira o valor do primeiro segmento: '))
cd = float(input('Insira o valor do segundo segmento: '))
ef = float(input('Insira o valor do terceiro segmento: '))

#VERIFICADOR DE FORMAÇÃO DE TRIANGULO E TIPO;

if ab+cd>ef and cd+ef>ab and ab+ef>cd:
    print('É possível formar um triângulo!', end=' ')
    if ab == cd == ef:
        print('O Triângulo é EQUILÁTERO!')
    elif ab == cd != ef or cd == ef != ab or ef == ab != cd:
        print('O Triângulo é ISÓSCELES!')
    else:
        print('O Triângulo ESCALENO')
else:
    print('Não é possível formar um triângulo..')
