quantidade_de_numeros = int( input( 'Quamtos números: '))
pares = []
divisores_por_2_e_3 = []

for n in range( quantidade_de_numeros):
    numero = int( input( f'Número { n + 1}º: '))
    
    if numero % 2 == 0:
        pares.append( numero)
        
        if numero % 3 == 0:
            divisores_por_2_e_3.append( numero)

print( f'Os números pares são { pares}.')
print( f'Os divisões de 2 e 3 foram { divisores_por_2_e_3}.')

