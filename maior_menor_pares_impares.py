import random

lista = [ random.randint( 1, 1000) for n in range( 50)]
pares = []
impares = []
maior = menor = lista[ 0]

for n in range( len( lista)):
    
    if lista[ n] % 2 == 0:
        pares.append( lista[ n])
        
    if lista[ n] % 2 != 0:
        impares.append( lista[ n])
        
    if lista[ n] > maior:
        maior = lista[ n]
    
    if lista[ n] < menor:
        menor = lista[ n]

print()
print( 'Os números sorteados foram: ')
print( lista)
print()

print( 'Os números pares são: ')
print( pares)
print()

print( 'Os números ímpares são: ')
print( impares)
print()

print( 'O maior número é: ')
print( maior)

print( 'O menor número é: ')
print( menor)

