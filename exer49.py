posicao = int (input("qual posicao do fino voce quer saber: "))


termo1 = 1
termo2 = 1
fib = 0

controle = 2
print (termo1, end="\t")
print (termo2, end="\t")
while(controle < posicao):
    fib = termo1 + termo2
    termo1 = termo2
    termo2 = fib
    print (fib, end="\t")

    controle+=1