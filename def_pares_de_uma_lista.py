def pares( a):
    lista_de_pares = []
    for numero in a:
        if numero % 2 == 0:
            lista_de_pares.append( numero)
    
    return lista_de_pares


lista_de_numeros = []
while True:
    lista_de_numeros.append( int( input( 'Digite o número: ')))
    continuar = str( input( 'Continuar( S/N): ')).upper()
    print()
    
    if continuar == 'N':
        break
        

print( f'Os números digitados foram { lista_de_numeros}.')
print( f'Os números pares são pares { pares( lista_de_numeros)}.')
