pares = 0
impares = 0


for i in range(10):
    numero = int(input(f"digite {i+1}° numero inteiro: "))

    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1

print(f"\nquantidade de numeros pares: {pares}")
print(f"\nquantidade de numeros imapres: {impares}")            

