nomecomp = str(input('Insira seu nome completo: ')).lower().strip().split()
verificador = 'silva' in nomecomp
print('O seu nome possui silva? {}'.format(verificador))

'''Realiza a verificação se o nome inserido possui SILVA no nome completo, 
portanto se possui ela é verdadeira, caso contrário é falsa'''