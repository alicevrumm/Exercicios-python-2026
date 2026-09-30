
a = int(input("Informe o valor de 'A': "))
b = int(input("Informe o valor de 'B': "))
c = int(input("Informe o valor de 'C': "))
 
delta = 0 

if (a == 0):
    print("[1;31;40mEssa equação não é de segundo grau.[m")
else:
    delta = (b*b) - (4*a) * c
    if(delta < 0):
       print("[1;31;40mA equação não possui raízes.[m")
    elif(delta == 0):
        print("[1;31;40mA equação possui apenas uma raíz real.[m")
    else:
        print("[1;31;40mA equação possui duas raízes.[m")