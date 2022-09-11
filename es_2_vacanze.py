colori = {"nero": 0,"marrone": 1,"rosso": 2,"arancione": 3,"giallo": 4,"verde": 5,"blu":6,"viola":7,"grigio":8,"bianco":9}
res,ris = [],""
print("inserisci i colori della resistenza")
for k in range(3):
    res.append(input())

for colore in res:
    ris += str(colori[colore])
print(f"la resistenza è da: {ris}")