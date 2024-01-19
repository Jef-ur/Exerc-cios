lista_de_produtos = []
lista_de_precos = []

while True:
    lista_de_produtos.append( str( input( 'Produto: ')))
    lista_de_precos.append( float( input( 'Preço: ')))
    
    continuar = str( input( 'Continuar( S/N): ')).upper()
    print()
    if continuar == 'N':
        break 

maior_preco = lista_de_precos[ 0]
menor_preco = lista_de_precos[ 0]

for preco in lista_de_precos:
    if preco > maior_preco:
        maior_preco = preco
    
    if preco < menor_preco:
        menor_preco = preco

print( f'O maior preço é { maior_preco}.')
print( f'O menor preço é { menor_preco}.')
