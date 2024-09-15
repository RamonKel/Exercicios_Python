print('-=' * 8)
print(' MÉDIA ESCOLAR ')
print('-=' * 8)

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1+nota2)/2

print('A soma da nota {:.1f} mais a nota {:.1f} resulta na média {:.1f}, portanto..'.format(nota1,nota2,media))
if media > 7:
    print('Parabens! Você foi \033[1;32;40m APROVADO \033[m!')
elif media >= 5 and media <= 6.9:
    print('Você infelizmente está de \033[1;33;40mRECUPERAÇÃO\033[m..')
else:
    print('Você está \033[1;31;40m REPROVADO \033[m, quem sabe na próxima..')
