wort = input("Was möchtest du sagen? ")
anzahl = input("Wie oft möchtest du es sagen? ")
for nummer in range(eval(anzahl)):
    print(wort, end=" ")
