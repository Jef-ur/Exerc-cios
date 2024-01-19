senha = str( input( 'Senha: '))

maiuscula = any( n.isupper() for n in senha)
numero = any( n.isdigit() for n in senha)

for n in senha:
    if len( senha) < 8 or not maiuscula or not numero:
        print( f'A senha { senha} não é válida.')
        break
    
else:
    print( f'A senha { senha} é válida.')
