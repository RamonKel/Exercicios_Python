from datetime import date

print('-=' * 16)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=' * 16)

ano = int(input('Digite o ano que o atleta nasceu: '))

calculo_idade = date.today().year - ano

print('O atleta tem {} anos'.format(calculo_idade))

if calculo_idade < 9:
    print('Classificação: MIRIM')
elif calculo_idade >= 9 and calculo_idade <= 14:
    print('Classificação: INFANTIL')
elif calculo_idade >= 14 and calculo_idade <= 19:
    print('Classificação: JUNIOR')
elif calculo_idade >= 19 and calculo_idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
