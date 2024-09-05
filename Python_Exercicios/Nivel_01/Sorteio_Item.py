import random

lista_alunos = []
lista_alunos.append(input('Insira o nome do primeiro aluno: '))
lista_alunos.append(input('Insira o nome do segundo aluno: '))
lista_alunos.append(input('Insira o nome do terceiro aluno: '))
lista_alunos.append(input('Insira o nome do quarto aluno: '))

print('O aluno escolhido para lider foi {}'.format(lista_alunos[random.randint(0,1)]))
print('O aluno escolhido para apagar o quadro foi {}'.format(random.choice(lista_alunos)))

#Realiza o sorteio de algum nome da lista, utilizando a biblioteca random