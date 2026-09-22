num1 = int(input("Informe o primeiro número: "))
operacao = input("Operação [+]   [-]     [*]     [/]: ")
num2 = int(input("Informe o segundo número: "))

if operacao == "+":
    print("Resultado:", num1 + num2)
elif operacao == "-":
    print("Resultado:", num1 - num2)
elif operacao == "*":
    print("Resultado:", num1 * num2)
elif operacao == "/":
    print("Resultado:", num1 / num2)
else:
    print("Operação inválida!")