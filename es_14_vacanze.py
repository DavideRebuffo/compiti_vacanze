codice = "4539319503436467"
somma = 0
for k,lettera in enumerate(codice):
    if k % 2 == 0:
        if 2*int(lettera) > 9: somma+= 2*int(lettera)-9
        else: somma+= 2*int(lettera)
    else : somma+= int(lettera)

if somma % 10 == 0: print("il codice è verificato")
else: print("il codice non è verificato")
