import random
notAvaiable,risp = [],"si"
while risp == "si": 
    nomeRobot = chr(random.randint(65,90)) + chr(random.randint(65,90)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    if nomeRobot in notAvaiable: print("nome non disponibile")
    else: 
        print(nomeRobot)
        notAvaiable.append(nomeRobot)
    risp = input("vuoi continuare? ").lower()
