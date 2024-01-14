lado1 = int( input( 'Primeiro lado: '))
lado2 = int( input( 'Segundo lado: '))
lado3 = int( input( 'Terceiro lado: '))

if lado1 == lado2 == lado3:
    print( 'Equilátero.')
    
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print( 'Isósceles.')

else:
    print( 'Escaleno.')

