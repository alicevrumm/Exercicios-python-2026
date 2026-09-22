#(Com estrutura de repetição) Faça um algoritmo que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int (input("digite o primeiro numero: "))
n2 = int (input("digite o segundo numero: "))

# for n in range(n1, n2, 5):
#     print(n)

if(n1<=n2):
 for n in range(n1+1, n2):
    print(n)
else:
  for n in range(n2+1, n1):
    print(n)    