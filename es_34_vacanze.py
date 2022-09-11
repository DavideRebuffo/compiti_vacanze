lista = [1,[2,3,"null",4],["null"],5]
listaNuova = []
for cella in lista:
    if type(cella) == list: 
        for pezzo in cella:
            if pezzo != "null": listaNuova.append(pezzo)
    else: listaNuova.append(cella)
print(listaNuova)