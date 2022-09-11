class Allergia:
    def __init__(self,punteggio):
        self.punteggio = punteggio
        self.dizio = {"cats":128 , "pollen":64,"chocolate":32, "tomatoes":16, "strawberries":8, "shellfish":4, "peanuts":2,"eggs":1}
    def isAllergico(self, oggetto):
        return self.punteggio - self.dizio[oggetto] > 0
    def listaAllergie(self):
        lista,num = [],self.punteggio
        while num != 0:
            for chiave in self.dizio:
                if num - self.dizio[chiave] >= 0: 
                    lista.append(self.dizio[chiave])
                    num = num - self.dizio[chiave]
        return lista

al = Allergia(34)
print(al.listaAllergie())
