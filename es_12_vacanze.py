while True:
    domanda = input("Tu: ")
    if domanda == "": print("Bob: Va bene. Sii così")
    elif domanda.lower() == "come stai?": print("Bob: Certo")
    elif domanda == domanda.upper() and domanda[-1] == "?": print("Bob: Calmati, so cosa sto facendo")
    elif domanda == domanda.upper(): print("Bob: Whoa rilassati!")
    else: print("Qualunque cosa")