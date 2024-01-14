print( '\033[1;32;40m_' * 49)

def validar_numero( a):
    while True:
        try:
            numero = int( input( a))
            return numero
        
        except( ValueError, TypeError):
            print()
            print( '\033[1;31;40mErro no tipo de dado.')
            print( 'Digite um número inteiro.\033[1;32;40m')
            print()
            

def antecessor( a):
    return a - 1
    

def sucessor( a):
    return a + 1


numero = validar_numero( 'Digite um número: ')
print()

print( f'O antecessor de { numero} é { antecessor( numero)}.')
print( f'E o sucessor de { numero} é { sucessor( numero)}.')

print( '\033[1;32;40m_' * 49)
