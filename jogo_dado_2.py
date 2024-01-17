import random

while True:
    dado1 = random.randint( 1, 6)
    dado2 = random.randint( 1, 6)
    valor = int( input( 'Qual valor: '))
    
    if valor == dado1 or valor == dado2:
        print( 'Parabens! Você acertou.')
    else:
        print( 'Infelizmente não foi esse número.')
    print( f'Os números sorteados: { dado1} e { dado2}.')
    print()
    
    continuar = str( input( 'Continuar( S/N): ')).upper()
    
    if continuar == 'N':
        break

