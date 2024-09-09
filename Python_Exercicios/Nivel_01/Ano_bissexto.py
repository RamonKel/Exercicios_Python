from datetime import date

print('-=' * 10)
print('ANO BISSEXTO')
print('-=' * 10)

ano = int(input('Digite um ano: (Aperte 0 para o ano atual): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

'''Realiza a verificação se um ano é bissexto ou não de acordo com as especificações'''
