frase = str(input('Digite uma frase: ')).lower().strip()

contagem = frase.count('a')
posicao_inicial =  frase.find('a') + 1 #Para usuários comuns a contagem inicia no 1, portanto realiza-se a soma
posicao_final =  frase.rfind('a') + 1

print('A letra A aparece {} vezes \n'
      'A primeira letra A aparece na posição {} \n'
      'A ultima letra A aparece na posição {}'.format(contagem,posicao_inicial,posicao_final))

'''Realiza a verificação de quantas letras A possui na frase, 
também realiza a localização da sua primeira e ultima aparição'''
