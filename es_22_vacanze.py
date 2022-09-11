numeroNonFormattato = "+1 (613)-995-0253"
finale = ""
for lettera in numeroNonFormattato:
    if lettera >= "0" and lettera <= "9": finale+= lettera

if finale.__len__() == 11 and finale[0] == "1": print(finale[1:])
else: print(finale)