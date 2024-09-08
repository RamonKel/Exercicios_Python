cidade = str(input('Digite a cidade que você nasceu: ')).lower().strip().split()
verificar = 'santo' in cidade[:5]
print('De acordo com a verificação você está.. {}'.format(verificar))

'''Realiza a verificação se a cidade inserida possui SANTO em seu inicio, 
portanto se possui ela é verdadeira, caso contrário é falsa'''