frase = str( input( 'Digite uma frase: ')).upper()

quantidade_de_vogais = 0
for letra in frase:
    if letra in 'AEIOU':
        quantidade_de_vogais += 1

print( f'A frase { frase} tem { quantidade_de_vogais} vogais.')
