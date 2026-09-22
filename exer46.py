#(Com estrutura de repetição) Faça um algoritmo que desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#TABUADA de 5:
#5 X 1 = 5
#5 X 2 = 10
#…
#5 X 10 = 50 

n1 = int (input("digite o numero: "))

for n in range (1, 11):
    print (f"{n1} x {n} = {n1*n}")