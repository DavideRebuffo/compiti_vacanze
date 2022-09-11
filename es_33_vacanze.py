enne,somma,sommaQuad = int(input("inserisci il numero di numeri: ")),0,0

for k in range(enne+1):
    somma+=k
    sommaQuad += k**2
print(f"la differenza è di: {somma**2-sommaQuad}")