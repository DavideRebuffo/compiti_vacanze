anno = int(input("inserisci un anno: "))

if anno % 400 == 0 or (anno % 4 == 0 and not(anno %100 == 0)): print("l' anno è bisestile")
else: print("l' anno non è bisestile")