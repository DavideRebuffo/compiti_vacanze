import random

def assegna():
    dadi = [random.randint(1,6) for _ in range(4)]
    dadi.remove(min(dadi))
    somma = 0
    for dado in dadi: somma+= dado
    return somma

class Character:
    def __init__(self):
        self.forza = assegna()
        self.destrezza = assegna()
        self.costruzione = assegna()
        self.intelligenza = assegna()
        self.saggezza = assegna()
        self.carisma = assegna()
        self.vita = 10 + int((self.costruzione-10)/2)
    def visualizzaCaratteri(self):
        print(f"forza: {self.forza}\ndestrezza: {self.destrezza}\ncostruzione: {self.costruzione}\nintelligenza: {self.intelligenza}\nsaggezza: {self.saggezza}\ncarisma: {self.carisma}\npunti vita: {self.vita}")

def main():
    myMonster = Character()
    myMonster.visualizzaCaratteri()

if __name__ == "__main__":
    main()