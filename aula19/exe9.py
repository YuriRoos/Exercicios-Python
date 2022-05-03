for c in range (1,6):
    aluno=input('aluno : ')
    n1=float(input('nota 1: '))
    n2=float(input('nota 2: '))

    media=(n1+n2)/2
    final=media>6

print('o total de alunos em nota final será de {}'.format(final))