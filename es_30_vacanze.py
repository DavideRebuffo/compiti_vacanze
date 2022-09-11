class Pila():
    def __init__(self):
        self.pila = []
        self.top3 = []
        self.last = 0
        self.top = 0
    def push(self,elemento):
        self.pila.append(elemento)
        self.last = elemento
        if elemento > self.top: self.top = elemento
        if self.top3.__len__() < 3: self.top3.append(elemento)
        elif elemento > self.top3[0]: self.top3 = [elemento,self.top3[0],self.top3[1]]
        elif elemento > self.top3[1]: self.top3 = [self.top3[0],elemento,self.top3[1]]
        elif elemento > self.top3[2]: self.top3 = [self.top3[0],self.top3[1],elemento]
    def pop(self):
        if self.pila.__len__() != 0:
            return self.pila.pop()
        else:
            return None
    def print(self):
        print(f"tutti i punteggi: {self.pila}\ntop3: {self.top3}\nmiglior punteggio: {self.top}\nultimo punteggio: {self.last}")

pila = Pila()
pila.push(1)
pila.push(1)
pila.push(1)
pila.push(5)
pila.push(1)
pila.push(1)
pila.push(3)
pila.push(1)
pila.print()
