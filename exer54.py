#Faça um algoritmo que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
cont25 = 0
cont50 = 0
cont75 = 0
cont100 = 0
while True:
    n = int (input("digite um numero(ou coloque - para sair): "))

    if (n < 0):
        break

    if (n >= 0 and n<25):
        cont25 = cont25 + 1

    elif (n >= 25 and n<50):
        cont50 = cont50 + 1

    elif (n >= 50 and n<75):
        cont75 = cont75 + 1
    else:
        cont100 = cont100 +1        
       
print("QUNATIDADE 0 - 25 =" , cont25)
print("QUNATIDADE 26-50 =" , cont50)
print("QUNATIDADE 51-75 =" , cont75)
print("QUNATIDADE 76-100 =" , cont100)


