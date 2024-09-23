soma = 0
cont = 0

for i in range(1,7):
    num = int(input('Digite o {}° valor: '.format(i)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Foi informado {} valores pares. A soma de todos valores pares é de {}'.format(cont,soma))
