area = float(("digite o tamanho da area em metros quadrados: "))

litros = area/ 3
latas= int (litros// 10)
if litros % 18>0:
    latas = latas + 1 

preco = latas * 80

print ("latas necessarias: ", latas)
print ("preço total: ", preco)