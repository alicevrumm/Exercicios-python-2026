#(Com estrutura de repetição)Faça um algoritmo que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n1 = int(input("digite um numero: "))
fat=1
for n in range (n1, 0, -1):
    fat = fat * n

print(fat)