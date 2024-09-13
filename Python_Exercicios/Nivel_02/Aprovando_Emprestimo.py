print('-=' * 13)
print('AVALIADOR DE EMPRÉSTIMO')
print('-=' * 13)

valor_casa = float(input('Digite o valor da casa: R$ '))
valor_salario = float(input('Digite o valor do salário: R$ '))
ano = int(input('Digite em quantos anos o emprestimo será feito: '))

prestacao = valor_casa/(ano * 12)

verificador = (valor_salario * 0.30)

print('Uma casa de {:.2f}, em {} anos, sua prestação mensal é de {:.2f}'.format(valor_casa,ano,prestacao))

if prestacao > verificador:
    print('O valor minimo excede a prestação.. \033[1;31;40m NEGADO \033[m')
else:
    print('Emprestimo \033[1;32;40m APROVADO \033[m')
