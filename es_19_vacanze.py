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
    ennesimo = int(input("inserisci un numero: "))
    primi,k = 0,1
    while primi < ennesimo:
        k+=1
        if isPrimo(k): 
            primi+= 1
    print(f"il {ennesimo}° numero primo è: {k}")

if __name__ == "__main__":
    main()