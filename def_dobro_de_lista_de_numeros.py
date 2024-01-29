def dobro( a):
    for n in range( len( a)):
        a[ n] *= 2
    
    return a


lista_de_numeros = []
while True:
    lista_de_numeros.append( int( input( 'Digite um número: ')))
    continuar = str( input( 'Continuar: ')).upper()
    
    if continuar == 'N':
        break
        

print( f'Os números digitados são: { lista_de_numeros}.')
print( f'E o dobro é: { dobro( lista_de_numeros)}.')

