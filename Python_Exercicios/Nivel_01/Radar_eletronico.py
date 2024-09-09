from time import sleep

print('-=' * 15)
print('ORGÃO FEDERAL DE TRÂNSITO')
print('-=' * 15)

velocidade = float(input('Digite a velocidade do carro: (Km/h) '))
multa = (velocidade - 80) * 7

print('Processando...')
sleep(3)

if velocidade > 80:
    print("MULTADO! você ultrapassou a velocidade máxima de 80 Km/h")
    print('Sua multa é de R$ {}'.format(multa))

print('Tenha um ótimo dia! Dirija com segurança!')

'''Realiza a verificação da velocidade do carro, e com uma estrutura condicional
simples, verifica se está dentro dos limites, até mesmo realizando o calculo 
da multa excedido (Sendo R$ 7 por cada Km/h excedido)'''
