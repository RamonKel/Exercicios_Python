print('-=' * 15)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-=' * 15)

numero = int(input('Digite um valor inteiro: '))
base = int(input('Qual base deseja converter? \n'
                 '\033[1;31;40m [ 1 ] converter para BINÁRIO \033[m\n'
                 '\033[1;32;40m [ 2 ] converter para OCTAL \033[m\n'
                 '\033[1;33;40m [ 3 ] converter para HEXADECIMAL \033[m\n'
                 'Sua opção: '))

if base == 1:
    print('O numero {} em BINÁRIO é {} '.format(numero, bin(numero)))
elif base == 2:
    print('O numero {} em OCTADECIMAL é {} '.format(numero, oct(numero)))
elif base == 3:
    print('O numero {} em HEXADECIMAL é {} '.format(numero, hex(numero)))
