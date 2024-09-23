num_primo = int(input('Digite um valor: '))
total = 0

for i in range(1, num_primo + 1):
    if num_primo % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n O número {} foi divisível por {} números'.format(num_primo,total))
