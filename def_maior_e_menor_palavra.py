def maior_palavra( a):
    quantidade_de_letras = 0
    maior_palavra = ''
    for palavra in a:
        if len( palavra) > quantidade_de_letras:
            quantidade_de_letras = len( palavra)
            maior_palavra = palavra
    
    return maior_palavra


def menor_palavra( a):
    quantidade_de_letras = len( a[ 0])
    menor_palavra = ''
    for palavra in a:
        if len( palavra) < quantidade_de_letras:
            quantidade_de_letras = len( palavra)
            menor_palavra = palavra
    
    return menor_palavra


lista_de_palavras = []
while True:
    lista_de_palavras.append( str( input( 'Digite uma palavra: ')))
    continuar = str( input( 'Continuar( S/N): ')).upper()
    print()
    if continuar == 'N':
        break


print( f'A maior palavra é { maior_palavra( lista_de_palavras)}.')
print( f'Com { len( maior_palavra( lista_de_palavras))} letras.')
print( f'A menor palavra é { menor_palavra( lista_de_palavras)}.')
print( f'Com { len( menor_palavra( lista_de_palavras))} letras.')
