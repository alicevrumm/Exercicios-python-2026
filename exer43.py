#for numeros in range(1,50,2):
primos= int(input("digite o numero: "))

primos = []

for n in range(2, num+1):
    primo = True

    for x in range(2,n):
        if n%x==0:
            primo = False
            break

    if primo:
       primos.append(n)

print(primos)