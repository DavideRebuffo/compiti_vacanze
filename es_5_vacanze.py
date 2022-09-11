stringa = input("inserisci una frase: ")
uscite = []

for lettera in stringa:
    uscite.append(lettera)
    if lettera in uscite[:-1]: 
        print("la stringa non è isogramma")
        break
if uscite.__len__() == stringa.__len__(): print("la stringa è isogramma")