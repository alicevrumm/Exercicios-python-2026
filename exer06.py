num1 = int(input("digite o 1 numero: "))
num2 = int(input("digite o 2 numero: "))

ope = (input("digite a soma desejada + ou -: "))

if(ope == "+"):
  resul = (num1 + num2)
  print ("a soma dos numeros é: ", str(resul))
else:
  resul = (num1 - num2)
  print ("a subtração dos numeros é: ", str(resul))