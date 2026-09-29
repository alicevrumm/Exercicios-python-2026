#Faça um algoritmo que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("digite o numero: "))

primos = []

for n in range(2, num+1):
    primo = True
    #print(n)
    #print("\nN->", n)
    for x in range(2,n):
        #print("\t")
        #print(x, end="\t")
        if n%x==0:
            primo = False
            break

    if primo==True:
       primos.append(n)

print(primos)       