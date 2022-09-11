lettereZeri, lettereNonZeri = ["I","X","C","M"],["V","L","D"]

def trasforma(numero, posizioni):
    romano = ""
    if numero == 1: romano+= lettereZeri[posizioni]
    elif numero == 2: romano+= lettereZeri[posizioni]*2
    elif numero == 3: romano+= lettereZeri[posizioni]*3
    elif numero == 4: romano+= lettereNonZeri[posizioni] + lettereZeri[posizioni-1]
    elif numero == 5: romano+= lettereNonZeri[posizioni]
    elif numero == 6: romano+= lettereNonZeri[posizioni] + lettereZeri[posizioni]
    elif numero == 7: romano+= lettereNonZeri[posizioni] + lettereZeri[posizioni]*2
    elif numero == 8: romano+= lettereNonZeri[posizioni] + lettereZeri[posizioni]*3
    elif numero == 9: romano+= lettereNonZeri[posizioni] + lettereZeri[posizioni]
    return romano

def main():
    decimale = input("inserisci un numero da convertire: ")
    romano = ""
    for k in range(decimale.__len__()):
        romano+= trasforma(int(decimale[k]),int(decimale.__len__()-(k+1)))
    print(romano)

if __name__ == "__main__":
    main()
