# Programm Code für eine theoretische Einführung

## Ideen Didaktik
- Beamer mit Live Coding
- Legosteine > Module
- Eisenbahn > Programm-Fluss

## Themen

### Kommentare

~~~python
# Dies wird von Python nicht gelesen
# Ich kann hier schreiben was ich will
~~~

### Variablen
- Variablen sind wie Schachteln

~~~python
nummer = 1
wort = "Hallo"
liste_mit_nummern = [1, 2, 3, 4, 5]
liste_mit_strings = ["Eins", "Zwei", "Drei"]
~~~

### Print und Input

~~~python
name = "Sophia"
print(name)
~~~

~~~python
name = input("Wie heißt du? ")
print(name)
~~~

### Import

~~~python
import turtle
turtle.bgcolor("black")
schildkroete = turtle.Pen()
schildkroete.pencolor = "red"
schildkroete.width = 5
schildkroete.forward(100)
turtle.Screen().exitonclick()
~~~

~~~python
import random
würfelzahl = random.randint(1,6)
~~~

### Schleifen

~~~python
for x in range(10):
    print("Hallo")

namen = ["Wenzai", "Ifeoma", "Eleny", "Kristin"]
for name in namen:
    print ("Hallo " + name + "!")
~~~

### Funktionn

~~~python
def gruss():
    print("Hallo")
~~~

### Bedingungen

~~~python
print("Was ist 1 + 1?")
input(ergebnis)
if ergebnis == 2:
    print("Richtig")
else:
    print("Falsch")
~~~

