#print('\033[1;31;40mTeste\33[m')
#letra = input("digite S para SIM e N para NAO: ")[0]
#print(letra)
palavra = (input("digite uma palavra: "))
print(f'{palavra.upper()} e tem {len(palavra)} de letras')

palavra = palavra + palavra[::-1]
print (palavra)

print(palavra.split(' '))