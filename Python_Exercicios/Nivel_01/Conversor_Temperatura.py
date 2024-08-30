C = float(input('Digite a temperatura atual em Celsius (C°): '))
F = (C * 1.8) + 32 #Fahrenheit calc
K = C + 273 #Kelvin calc
print('O valor em Celsius é de °C {:.2f}, convertendo para Fahrenheit se torna °F {:.2f}'.format(C,F))
print('O valor em Celsius é de °C {:.2f}, convertendo para Kelvin se torna °F {:.2f}'.format(C,K))

# Faz a conversão do valor da temperatura em Celsius para Fahrenheit e Kelvin