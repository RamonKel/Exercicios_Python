h = float(input('Digite a altura da sua parede em metros (M): '))
l = float(input('Digite a largura da sua parede em metro (M): '))
Area = h*l #Calculo da área da parede
Tinta = Area/2 #Calculo de quanto de tinta será utilizado de acordo com a área

print('Sua parede possui {} x {}, e sua área é {:.2f}m²'.format(h,l,Area))
print('Para pintar a parede de {}m², é necessário utilizar {:.2f}l de tinta'.format(Area,Tinta))
