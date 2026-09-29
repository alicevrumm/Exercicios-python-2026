el = int (input("digite quantos eleitores vao votar: "))

candA = 0
candB = 0
candC = 0
i = 0
while (i<el):
    i = i+1
    resp= input(f"{i} VOTO: Em quem voce vai votar?(A) (B) (C): ")[0].upper()
    if (resp == "A"):
        candA=candA+1
    elif (resp == "B"):
        candB = candB+1
    elif (resp == "C"):
        candC = candC +1
    else:
        print ("tudo nulo")            

if  (candA > candB and candA > candC):
        print ("vencedora........... AAAAAAAAAAA")

elif  (candB > candA and candB > candC):
        print ("vencedora........... BBBBBBBBBBBBBBBBB")

elif  (candC > candA and candC > candB):
        print ("vencedora........... CCCCCCCCCCCC")
else:
    if  (candA == candB ):
        print ("EMPATE entre CAND A e CAND B")
    elif  (candA == candC ):
        print ("EMPATE entre CAND A e CAND C")
    else:
        print ("EMPATE entre CAND B e CAND C")
    
