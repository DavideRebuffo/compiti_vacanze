dna1,dna2 = input("inserisci il primo fascio di dna: "),""
while dna2.__len__() != dna1.__len__():
    dna2 = input("inserisci il secondo fascio di dna: ")
hamming = 0
for k,lettera in enumerate(dna1):
    if lettera != dna2[k]: hamming+=1

print(f"il numero di hamming è {hamming}")
