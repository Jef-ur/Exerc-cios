import random

dado1 = random.randint( 1, 6)
dado2 = random.randint( 1, 6)
valor = int( input( 'Qual número foi sorteado: '))

if dado1 == valor or dado2 == valor:
    print( 'Parabéns! Você acertou.')
    
else:
    print( 'Infelizmente não foi esse número.')

print( f'Os números sorteados foram { dado1} e { dado2}.')