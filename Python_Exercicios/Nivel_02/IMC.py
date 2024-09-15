from math import pow

print('-=' * 12)
print('ÍNDICE DE MASSA CORPORAL')
print('-=' * 12)

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso/pow(altura,2)

print('Seu indice de massa corporal é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Classificação: Baixo Peso')
elif 18.5 <= imc < 24.9:
    print('Classificação: Normal')
elif 25 <= imc < 29.9:
    print('Classificação: Sobrepeso')
elif 30 <= imc < 39.9:
    print('Classificação: Obesidade')
else:
    print('Classificação: Obesidade Mórbida')
