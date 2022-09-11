stringa = input("inserisci una stringa: ")
lunghezza = int(input("inserisci la lunghezza delle sottostringhe: "))

for k in range(stringa[:-lunghezza+1].__len__()):
    print(stringa[k:k+lunghezza])