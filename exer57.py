#(Com estrutura de decisão) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
qtresp = 0
print("RESPONDA [S]im ou [N]ão para as perguntas")
resp =  ((input("telefonou para a vitima:? ")).upper())[0]
if (resp == "S"):
    qtresp = qtresp + 1

resp =  ((input("Esteve no local do crime:? ")).upper())[0]
if (resp == "S"):
    qtresp = qtresp + 1

resp =  ((input("Mora perto da vítima:? ")).upper())[0]
if (resp == "S"):
    qtresp = qtresp + 1

resp =  ((input("Devia para a vítima:? ")).upper())[0]
if (resp == "S"):
    qtresp = qtresp + 1

resp =  ((input("Já trabalhou com a vítima:? ")).upper())[0]
if (resp == "S"):
    qtresp = qtresp + 1     

if (qtresp == 0):
    print ("inocente")

elif (qtresp == 1):
    print ("inocente")

elif (qtresp == 2):
    print ("suspeito")

elif (qtresp == 3):
    print ("cumplice")

elif (qtresp == 4):
    print ("cumplice")

elif (qtresp == 5):
    print ("assassino")               