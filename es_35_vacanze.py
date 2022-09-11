dizio = {"Methionine":["AUG"],"Phenylalanine":["UUU", "UUC"],"Leucine":["UUA", "UUG"],"Serine":["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine":["UAU", "UAC"],"Cysteine":["UGU", "UGC"],"Tryptophan":["UGG"],"STOP":["UAA", "UAG", "UGA"]}
codone = "AUGUUUUCU"

listaCodone,listaProteine = [],[]
for k in range(0,codone.__len__(),3):
    listaCodone.append(codone[k:k+3])

for cella in listaCodone:
    for chiave in dizio:
        if cella in dizio[chiave]: listaProteine.append(chiave)

print(listaProteine)