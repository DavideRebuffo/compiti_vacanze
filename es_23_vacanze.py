pos1 = input("inserisci la posizione della prima regina: ")
pos2 = input("inserisci la posizione della seconda regina: ")
dizio = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
if pos1[0] == pos2[0] or pos1[1] == pos2[1]: print("le regine si possono scontrare")

#c5     f2
if int(pos1[1]) > int(pos2[1]):
    if int(pos1[1]) - int(pos2[1]) == dizio[pos2[0]] - dizio[pos1[0]]: print("le regine si possono scontrare")
elif  int(pos1[1]) < int(pos2[1]):
    if int(pos2[1]) - int(pos1[1]) == dizio[pos1[0]] - dizio[pos2[0]]: print("le regine si possono scontrare")
elif pos1 == pos2: print("le regine si possono scontrare")
else: print("le regine non si possono scontrare")