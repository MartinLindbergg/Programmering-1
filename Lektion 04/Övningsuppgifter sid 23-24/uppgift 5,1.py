#inmatning
indata = input ("Skriv in ett heltal tal:")
#Funktion
try:
    #gör om indata till en integer
    indata = int(indata)
    #gångrar inmatade talet med 2
    times_2 = indata * 2
    #skriver ut inmatade talet och skriver ut det inmatade talet * 2
    print("Tal:" , indata)
    print("Resultat:", times_2)
# felhantering, om inmatningen är annat än ett tal skriver programmet ut ett felmeddelande
except ValueError:
    print(indata , "kan inte översättas till ett heltal")






