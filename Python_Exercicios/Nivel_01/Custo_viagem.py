print('-=' * 10)
print('CUSTOS DE VIAGEM')
print('-=' * 10)

distancia = float(input('Digite a distância da viagem desejada: '))
calculo_distancia_curta = distancia * 0.50
calculo_distancia_longa = distancia * 0.45

print('Você está prestes a iniciar uma viagem de {} Km'.format(distancia))

if distancia <= 200:
    print('O custo da viagem será de R$ {:.2f}'.format(calculo_distancia_curta))
else:
    print('O custo da viagem será de R$ {:.2f}'.format(calculo_distancia_longa))

'''Realiza o calculo de custos de uma viagem, de acordo com a quantidade de Km,
Se for até 200km o preço é de 0,50 centavos, caso seja acima disso o valor diminui
para 0,45 centavos.'''
