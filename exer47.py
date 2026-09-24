#(Com estrutura de repetição) Faça um algoritmo que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.

n1= int (input("digite o primeiro numero: "))
n2= int (input("digite o segundo numero: "))
i=0
result = 1
while (i<n2):
    result= result*n1
    i = i+1

print (result)