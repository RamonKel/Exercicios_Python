d = float(input('Digite uma distância em metros(M): '))

print('A medida {} corresponde a:'.format(d))

print('Em Kilometro(Km)',d/1000)
print('Em Hectômetro(Hm)',d/100)
print('Em Decâmetro(Dam)',d/10)
print('Em Decimetro(Dam) {:.0f}'.format(d*10))
print('Em Centímetro(Hm) {:.0f}'.format(d*100))
print('Em Milímetro(Km) {:.0f}'.format(d*1000))

# Faz a conversão para as outras medidas de acordo com o valor definido