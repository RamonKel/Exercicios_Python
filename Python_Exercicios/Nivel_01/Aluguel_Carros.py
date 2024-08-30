Dia = int(input('Quantos dias o carro foi utilizado?(R$ 60/dia): '))
Km = float(input('Quantos Km foram percorridos?(R$ 0.15/Km): '))
Valor_dia = Dia*60
Valor_Km = Km*0.15
print('O total a pagar é R$ {:.2f}'.format(Valor_Km+Valor_dia))