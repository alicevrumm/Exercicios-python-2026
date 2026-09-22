anoN = int (input("digite o seu ano de nascimento: "))
anoA = int (input("digite o ano atual: "))
res = str (input("já foi seu aniversario?: "))
#idadeA = i nt


if (res == "sim" or res == "Sim"):
   idadeA = anoA - anoN
   idadeM = idadeA*5
   idadeD = idadeA*365.25
   ida2019 = idadeA - 7
else:
   idadeA = anoA - anoN
   idadeM = idadeA*5
   idadeD = idadeA*365.25-1
   ida2019 = idadeA - 7

print ("sua idade é: ", idadeA)
print (" em meses: ", idadeM)
print (" em dias: ",idadeD)
print (" e em 2019 era: ", ida2019)