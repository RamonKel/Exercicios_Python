print('='* 19)
print('10 TERMOS DE UMA PA')
print('='* 19)


primeiro_termo = int(input('Digite o valor do primeiro termo: '))
step = int(input('Digite a razão: '))
stop = primeiro_termo + (10-1) * step

for i in range(primeiro_termo,stop + step,step):
    print(i, end=' -> ')
print('ACABOU')
