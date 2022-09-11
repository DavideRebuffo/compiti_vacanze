stringa = input("inserisci una stringa: ") + " "
numero = 0
finale = ""
let = stringa[0]
for k,lettera in enumerate(stringa):
    if lettera != let and k != 0:
        if numero == 1: finale+= let
        else: finale+= str(numero) + let
        let = lettera
        numero = 1
    else: numero+=1

print(finale)
