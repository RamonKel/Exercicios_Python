nome = str(input('Digite seu nome completo: ')).strip().split()

primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print('Muito prazer em te conhecer! \n'
      'Seu primeiro nome é {} \n'
      'Seu ultimo nome é {}'.format(primeiro_nome,ultimo_nome))
