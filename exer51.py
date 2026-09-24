num = int(input("digite o numero: "))
primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % 1 == 0:
            primo = False

if primo:
    print ("verdadeiro")
else:
    print("falso")                    