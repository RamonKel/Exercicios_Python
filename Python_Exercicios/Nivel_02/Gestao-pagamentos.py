print('-=' * 16)
print(' EMPRESA MULTINACIONAL DE INFRA ')
print('-=' * 16)

valor_compra = float(input('Insira o valor das compras: R$ '))
metodo_pagamento = int(input('[ 1 ] à vista dinheiro/cheque \n'
                             '[ 2 ] à vista no cartão \n'
                             '[ 3 ] em até 2x no cartão \n'
                             '[ 4 ] 3x ou mais no cartão \n'
                             'Insira o método de pagamento: '))

if metodo_pagamento == 1:
    print('O valor da sua compra à vista dinheiro/cheque, com desconto ficará R$ {:.2f}'.format(valor_compra*0.90))
elif metodo_pagamento == 2:
    print('O valor da sua compra à vista no cartão, com desconto ficará R$ {:.2f}'.format(valor_compra*0.95))
elif metodo_pagamento == 3:
    print('O valor da sua compra em até 2x no cartão, ficará em 2x parcelas de R$ {:.2f} SEM JUROS'.format(valor_compra/2))
elif metodo_pagamento == 4:
    parcelas = int(input('Em quantas parcelas? (Mínimo 3x) '))
    print('O valor da sua compra em {} parcelas, ficará em R$ {:.2f} com os juros acrescidos \n'
          'O valor que de juros acrescidos no total é de R$ {:.2f}'.format(parcelas,(valor_compra*1.20)/parcelas,(valor_compra*1.20)- valor_compra))
else:
    print('Por favor selecione o método de pagamento correto..')