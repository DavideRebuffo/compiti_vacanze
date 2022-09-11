dizio = {"G":"C","C":"G","T":"A","A":"U"}
stringa = input("inserisci un fascio DNA: ")
modifiche = ""
for lettera in stringa: 
    modifiche+=dizio[lettera]

print(modifiche)
