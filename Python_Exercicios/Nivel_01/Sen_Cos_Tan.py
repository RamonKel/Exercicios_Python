from math import cos,sin,tan,radians, ceil

angulo = float(input('Digite o angulo desejado: '))

tangente = tan(radians(angulo))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))

print('O angulo de {:.1f}, em seno é de {:.2f}'.format(angulo,seno))
print('O angulo de {:.1f}, em cosseno é de {:.2f}'.format(angulo,cosseno))
print('O angulo de {:.1f}, em tangente é de {:.2f}'.format(angulo,tangente))

#De acordo com o valor do angulo inserido, é calculado o valor do Seno ,Cosseno e Tangente