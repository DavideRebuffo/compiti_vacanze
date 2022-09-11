class Matrix:
    def __init__(self, stringa):
            self.matrix = [[int(k) for k in lettera.split()] for lettera in stringa.split("\n")]
    def visualizza(self):
        print(self.matrix)
    def righe(self, indice):
        return self.matrix[indice - 1]
    def colonne(self, indice):
        return [int(str(array)[indice-1])for array in self.matrix]

def main():
    matrice = Matrix("987\n532\n667")
    matrice.visualizza()
    print(matrice.righe(3))
    print(matrice.colonne(2)) #array[indice - 1]

if __name__ == "__main__":
    main()