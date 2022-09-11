import random
from collections import Counter

def main():
    dadi,punteggio,categoria = [random.randint(1,6) for _ in range(5)],0,input("inserisci la categoria: ")
    if categoria.lower() == "quali": 
        for dado in dadi:
            if dado == 1: punteggio+=1
    elif categoria.lower() == "due": 
        for dado in dadi:
            if dado == 2: punteggio+=2
    elif categoria.lower() == "tre": 
        for dado in dadi:
            if dado == 2: punteggio+=3
    elif categoria.lower() == "quattro": 
        for dado in dadi:
            if dado == 2: punteggio+=4
    elif categoria.lower() == "cinque": 
        for dado in dadi:
            if dado == 2: punteggio+=5
    elif categoria.lower() == "sei": 
        for dado in dadi:
            if dado == 2: punteggio+=6
    elif categoria.lower() == "tutto esaurito":
        if len(Counter(dadi).keys()) == 2 and Counter(dadi).values()[0] in [2,3]: punteggio == Counter(dadi).values()[0] * Counter(dadi).keys()[0] + Counter(dadi).values()[1] * Counter(dadi).keys()[1]
    elif categoria.lower() == "quattro di un tipo": 
        if len(Counter(dadi).keys()) == 2 and Counter(dadi).values()[0] in [1,4]: punteggio == Counter(dadi).values()[0] * Counter(dadi).keys()[0] + Counter(dadi).values()[1] * Counter(dadi).keys()[1]
    elif categoria.lower() == "piccola dritta":
        if dadi.sort() == [1,2,3,4,5]: punteggio = 30
    elif categoria.lower() == "grande rettilineo":
        if dadi.sort() == [2,3,4,5,6]: punteggio = 30
    elif categoria.lower() == "scelta":
        for dado in dadi: punteggio+= dado
    elif categoria.lower() == "yacht":
        if Counter(dadi).values().__len__() == 1: punteggio = 50
    print(f"il tuo punteggio è di: {punteggio}")


if __name__ == "__main__":
    main()