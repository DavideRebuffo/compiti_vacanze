verificato,lato1,lato2,lato3 = False,0,0,0

while verificato == False:
    lato1 = float(input("inserisci il primo cateto: "))
    lato2 = float(input("inserisci il secondo cateto: "))
    lato3 = float(input("inserisci l' ipotenusa: "))
    if lato1 + lato2 >= lato3 and lato2 + lato3 >= lato1 and lato3 + lato1 >= lato2: verificato = True

if (lato1 == lato2) & (lato2 == lato3): print("il triangolo è equilatero")
else: print("il triangolo non è equilatero")
if ((lato1 == lato2) & (lato3 != lato1)) or ((lato2 == lato3) &( lato1 != lato2)) or ((lato1 == lato3) & (lato2 != lato3)): print("il triangolo è equilatero")
else: print("il triangolo non è equilatero")
if (lato1 != lato2) & (lato2 != lato3) & (lato3 != lato1): print("il triangolo è scaleno")
else: print("il triangolo non è scaleno")