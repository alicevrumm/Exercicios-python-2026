#Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ÔNIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um algoritmo que leia uma sequência de caracteres, mostre e diga se é um palíndromo ou não.

palavra = (input("digite uma palavra: "))
#print(f'{palavra.upper()} e tem {len(palavra)} de letras')

palavra_invertida =palavra[::-1]
print (palavra)
if (palavra == palavra_invertida):
    print ("palindromo")

else:
    ("nao é")    

