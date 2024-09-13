from datetime import date

print('-=' * 10)
print('ALISTAMENTO MILITAR')
print('-=' * 10)

idade = int(input('Digite o ano do seu nascimento: '))
calculo_idade = (date.today().year - idade)
print('Quem nasceu em {} tem {} em {}'.format(idade, calculo_idade, date.today().year ))

if calculo_idade > 18:
    calculo_ano = calculo_idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(calculo_ano))
    print('Seu alistamento foi em {}'.format(date.today().year - calculo_ano))
elif calculo_idade < 18:
    calculo_novo = 18 - calculo_idade
    print('Você ainda irá se alistar')
    print('Seu alistamento será daqui {} anos, ou seja, em {}'.format(calculo_novo, date.today().year + calculo_novo))
elif calculo_idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
