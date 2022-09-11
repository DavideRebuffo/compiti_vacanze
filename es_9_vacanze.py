ISBN = "3-598-21508-8"
usabile, rovescia,ris = "",10,0
for k,lettera in enumerate(ISBN):
    if lettera != "-": usabile+= lettera

for lettera in usabile: 
    ris += int(lettera) * rovescia
    rovescia-=1

if ris % 11 == 0: print("l' ISBN è verificato")
else: print("l' ISBN non è verificato")