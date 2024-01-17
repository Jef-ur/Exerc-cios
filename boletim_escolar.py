quantidade_de_alunos = int( input( 'Quantos alunos: '))
lista = []

for n in range( quantidade_de_alunos):
    lista_temporaria = []
    nome = str( input( 'Nome: '))
    lista_temporaria.append( float( input( 'Nota 1: ')))
    lista_temporaria.append( float( input( 'Nota 2: ')))
    lista_temporaria.append( float( input( 'Nota 3: ')))
    lista_temporaria.append( float( input( 'Nota 4: ')))
    lista_temporaria.append(( sum( lista_temporaria) / 4))
    lista_temporaria.insert( 0, nome)
    lista.append( lista_temporaria)
    print()

print( '_' * 45)
for aluno in lista:
    print( f'Nome:  { aluno[ 0]}.')
    print( f'Nota1: { aluno[ 1]}.')
    print( f'Nota2: { aluno[ 2]}.')
    print( f'Nota3: { aluno[ 3]}.')
    print( f'Nota4: { aluno[ 4]}.')
    print( f'Media: { aluno[ 5]}.')
    print( '_' * 45)
    print()

