#utgår ifrån dessa variabler
antal_tal = 0
summa = 0.0

#UI
print(".: MATHLETE v2 .0 :.")
print("-------------------")

#funktion
while True:
    try:
        inmatning = input("Skriv ett tal> ")
        #Om användare matar in exit (oavsätt om det är med stora eller små bokstäver) avslutas programmet.
        if inmatning.lower() == 'exit':
            break
        #talet görs om till en integer
        tal = int(inmatning)
        #Räknar hur många tal som skrivits in
        antal_tal += 1
        #Räknar ut summan av alla tal eftersom den tar tal + tal + tal osv
        summa += tal
    #Felhantering, Om användare matar in något annat än ett heltal så får vi en kommentar
    except ValueError:
       print("FEL : Ogiltigt nummer")
#om atntal_tal är större än noll så delas summan på antal tal för att få medelvärdet
if antal_tal > 0:
    medelvarde = summa / antal_tal
#om summan inte är större än noll
else:
    medelvarde = 0.0
#ui som skriver ut resultaten
print("-------------------")
print("Kardinalitet :", antal_tal)
print("Summa :", summa)
print("Medelvärde :", medelvarde)
