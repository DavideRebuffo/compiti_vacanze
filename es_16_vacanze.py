inglese = input("insert a string in english: ")
vocali =  ["a","e","i","o","u"]
pigLatin = ""
isConsonante = lambda lettera: lettera >= "a" and lettera <="z" and lettera not in vocali
if isConsonante(inglese[0].lower()) and inglese[1:3].lower() == "qu": pigLatin = inglese[3:] + inglese[:3] + "ay"
elif isConsonante(inglese[0].lower()): pigLatin = inglese[1:] + inglese[0] + "ay"
elif inglese[0].lower() in vocali or inglese[:1].lower() in ["xr","yt"]: pigLatin = inglese+ "ay"
elif inglese.__len__() == 2 and inglese[-1] == "y": pigLatin = "y" + inglese[0] + vocali[0] + "y"

print(f"your string in pigLatin language is: {pigLatin}")



