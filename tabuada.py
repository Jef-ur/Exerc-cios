numero = int( input( 'Numero: '))

print( f'A tabuada de { numero}.')
print( '_' * 49)
for n in range( 1, 11):
    print( f'|{ numero} + { n:>2} = { numero + n:>2}|', end = '')
    print( f'|{ numero} * { n:>2} = { numero * n:>2}|', end = '')
    print( f'|{ numero} / { n:>2} = { numero / n:>2.2f}|', end = '')
    print( f'|{ numero} - { n:>2} = { numero - n:>2}|')
print( '_' * 49)


