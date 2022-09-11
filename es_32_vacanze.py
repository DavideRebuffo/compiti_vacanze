numero = int(input("inserisci un numero: "))
somma = 0
for lettera in str(numero):
    somma+= int(lettera)**str(numero).__len__()

if somma == numero: print("è un numero di Armstrong")
else: print("non è un numero di Armstrong")