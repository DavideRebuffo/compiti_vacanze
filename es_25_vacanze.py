lettera = input("inserisci una lettera: ").upper()
#ord("A") chr(65)
lato = (ord(lettera) - 65)
spaziCentro = 0
spaziLato = lato

for k in range(lato*2+1):
    if k == 0 or k == lato*2:
        print(chr(183)*spaziLato + chr(65) + chr(183)*spaziLato)
        spaziCentro+=1
        spaziLato-=1
    elif k < lato:
        print(chr(183)*spaziLato + chr(65+k) + chr(183)*spaziCentro + chr(65+k) + chr(183)*spaziLato)
        spaziCentro+=2
        spaziLato-=1
    elif k >= lato: 
        print(chr(183)*spaziLato + chr(65+int(spaziCentro/2)+1) + chr(183)*spaziCentro + chr(65+int(spaziCentro/2)+1) + chr(183)*spaziLato)
        spaziCentro-=2
        spaziLato+=1
