#(Com estrutura de decisão) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro.

com = (input("digite se for [a]lcool ou [g]asolina:").upper())[0]

if (com == "G"):
    lit = float(input("quantos litros será?: "))
    tot = 5.50 * lit
    if (lit <= 20):        
        desc = tot * 0.03
        print ("vai pagar ", desc ,"de gasolina")
    if (lit >= 21):
        desc = tot * 0.05
        print ("vai pagar ", desc ,"de gasolina")

elif (com == "A"):
    lit = float(input("quantos litros será?: "))
    tot = 3.90 * lit

    if (lit <= 20):
        desc = tot * 0.04
        print ("vai pagar ", desc ,"de alccol")
    if (lit >= 21):
        desc = tot * 0.06
        print ("vai pagar ", desc ,"de alcool")                         
