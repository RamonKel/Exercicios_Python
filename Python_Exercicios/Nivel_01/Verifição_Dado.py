n1 = input('Digite uma informação: ')
print('O tipo primitivo desse valor é: {}'.format(type(n1))) #Verifica o tipo primitivo(string pois o input sempre será str)
print('Possui somente espaços? {}'.format(n1.isspace())) #Verifica se possui somente espaços
print('É um numero? {}'.format(n1.isnumeric())) #Verifica se é um numero
print('É alfabetico? {}'.format(n1.isalpha())) #Verifica se é do alfabeto
print('Está em maiusculas? {}'.format(n1.isupper())) #Verifica se está somente em letras maiusculas
print('Está em minusculas? {}'.format(n1.islower()))  #Verifica se está somente em letras minusculas
print('Está capitalizada? {}'.format(n1.istitle())) #Verifica se a primeira letra está maiusculas