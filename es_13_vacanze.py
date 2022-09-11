dizioValori = {1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],2:["D", "G"],3:["B", "C", "M", "P"],
                4: ["F", "H", "V", "W", "Y"],5:["K"],8:["J", "X"],10:["Q","Z"]}

parola = input("inserisci una parola: ")
valoreParola = 0
for lettera in parola:
    for chiave in dizioValori:
        if lettera.upper() in dizioValori[chiave]: valoreParola+= int(chiave)

print(f"il valore della tua parola è: {valoreParola}")