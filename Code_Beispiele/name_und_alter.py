name_string = input("Hallo! Wie heißt du? ")
alter_string = input("Hallo " + name + "! Wieviele Jahre bist du alt? ")

alter = int(alter_string)

alter_tage = alter * 360
alter_stunden = alter_tage * 24
alter_minuten = alter_stunden * 60
alter_sekunden = alter_minuten * 60

print(name + ", du bist also " + str(alter) + " Jahre alt.")
print("Das sind ungefähr ", str(alter_tage), " Tage.")
print("Das sind ungefähr " + str(alter_stunden) + " Stunden.")
print("Das sind ungefähr " + str(alter_minuten) + " Minuten.")
print("Das sind ungefähr " + str(alter_sekunden) + " Sekunden.")

