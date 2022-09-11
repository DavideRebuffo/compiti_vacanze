inizio = input("inserisci la tua frase: ").upper()
acronimo = inizio[0]

for k,lettera in enumerate(inizio):
    if lettera == " " or lettera == "-": acronimo+= inizio[k+1]

print(f"acronimo: {acronimo}")