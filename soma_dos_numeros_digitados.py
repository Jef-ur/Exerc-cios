lista_de_numeros = []
soma = 0

while True:
    numero = int( input( 'Digute um número: '))
    lista_de_numeros.append( numero)
    soma += numero
    
    continuar = str( input( 'Continuar( S/N): ')).upper()
    print()
    if continuar == 'N':
        break

print( f'Os números são { lista_de_numeros}.')
print( f'A soma é { soma}.')



