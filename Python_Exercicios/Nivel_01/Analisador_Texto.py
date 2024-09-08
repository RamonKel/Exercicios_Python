from os.path import split

nome = str(input('Digite seu nome completo: ')) # Pedido da informação

print('Analisando o nome...')
maiuscula = nome.upper() #Variável que transforma letras em maiusculas
print('Seu nome em letras maiusculas é: {}'.format(maiuscula))

minuscula = nome.lower() #Variável que transforma letras em minusculas
print('Seu nome em letras minusculas é: {}'.format(minuscula))

contagem = len(nome) - nome.count(' ') #Variável que realiza a contagem do nome inserido e retira os espaços
print('Seu nome compelto possui {} letras'.format(contagem))

quantidade = nome.split() #Variável que divide o nome em listas
contagem2 = len(quantidade[0]) #Variável que busca o primeiro nome
print('Seu primeiro nome é {} e ele possui {} letras'.format(quantidade[0],contagem2))

#Analisador de textos verifica um nome e traz algumas informações sobre ele;