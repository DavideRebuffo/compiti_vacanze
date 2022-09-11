def isPrimo(numero):
    ok = True
    rovescio = numero-1    
    while (ok == True) & (rovescio > 1):
        if numero % rovescio == 0:
            ok = False
        rovescio-=1
    if rovescio == 0:
        ok = False
    return ok

def main():
    numero = int(input("inserisci un numero: "))
    listaPrimi = [k for k in range(2,numero) if isPrimo(k)]
    primi = []
    while numero != 1:
        for primo in listaPrimi:
            if numero % primo == 0:
                numero = numero / primo
                primi.append(primo)
                break
    print(f"i fattori primi di {numero} sono: {primi}")

if __name__ == "__main__":
    main()