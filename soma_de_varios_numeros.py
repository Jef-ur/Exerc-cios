quantidade_de_numeros = int( input( 'Quantos números: '))
soma = 0
for n in range( quantidade_de_numeros):
    numero = int( input( f'Digite { n + 1}⁰ número: '))
    soma += numero
    
print( f'A soma entre os números foi { soma}.')

