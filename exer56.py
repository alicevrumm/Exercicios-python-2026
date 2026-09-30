numeros1_19 =["zero","um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete","dezoito", "dezenove"]
numeros_dezenas=["zero","dez","vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
n = int (input("digite o numero: "))

numero_extenso=""

if(n/10 >0):
    pos = int(n/10)
    numero_extenso=numeros_dezenas[pos]

    if (n%10 > 0):
        pos = int(n%10)
        numero_extenso = numero_extenso + " e " + numeros1_19 [pos]

#print(n/10)

#print(n%10)

print(numero_extenso)

