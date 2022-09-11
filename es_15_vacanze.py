numero = int(input("nserisci un numero: "))
collatz = 0
while numero != 1:
    if numero % 2 == 0: numero = numero / 2
    else: numero = numero * 3 + 1
    collatz+=1

print(f"il nuemero di collatz è: {collatz}")