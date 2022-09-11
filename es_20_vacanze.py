regali = ["twelve Drummers Drumming", "eleven Pipers Piping"," ten Lords-a-Leaping", "nine Ladies Dancing"," eight Maids-a-Milking", "seven Swans-a-Swimming"," six Geese-a-Laying", "five Gold Rings", "four Calling Birds", "three French Hens", "two Turtle Doves", "and a Partridge in a Pear Tree.\n"]
giorni = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth","eleventh","twelfth"]
canzone = ""
for k in range(12):
    if k == 0: canzone += "On the " +  giorni[0] + " day of Christmas my true love gave to me: " + regali[::-1][0][4:]
    else: 
        elenco = ""
        for j in range(k,-1,-1):
            elenco+= regali[12-j-1] + ","
            print()
        canzone+=  "On the " +  giorni[k] + " day of Christmas my true love gave to me: " + elenco[:-1]

print(canzone)