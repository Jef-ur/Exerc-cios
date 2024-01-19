numero = int( input( 'Quantos termos: '))
primeiro = 0
segundo = 1

print( f'{ primeiro} { segundo} ', end = '')

for n in range( 2, numero):
    print( f'{ segundo} ', end = '')
    primeiro += segundo 
    segundo += primeiro
