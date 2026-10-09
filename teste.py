cod1,quan1,pre1 = input().split()
cod2,quan2,pre2  = input().split()
tot = (int(quan1)*float(pre1)+(int(quan2)*float(pre2)))
print (f"VALOR A PAGAR : R$ {tot:.2f}")