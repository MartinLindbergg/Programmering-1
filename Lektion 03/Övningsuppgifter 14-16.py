'''
# uppgift 3.1
lista = []
tal_1 = int(input ("Ange ett tal: "))
tal_2 = int(input ("Ange ännu ett tal: "))
tal_3 = int(input("Ange ett sista tal: "))
totalt = max (tal_1, tal_2, tal_3)
print("----")
print("Det största inmatade talet är:" total)


# uppgift 3.2
namn = str(input ("Ange ditt namn: "))
ålder = int(input("Ange din ålder: "))

tabell = {
    1:      14,
    2:      13,
    3:      12,
    4:      11.5,
    5-6:    11,
    7:      10.5,
    8-10:   10,
    11:     9.5,
    12-15:  9,
    16:     8.5,
    "17+":    8
}

if ålder in tabell:
    sömnbehov = tabell[ålder]

else:
    sömnbehov = "okänt"

print(f"Hej {namn}! Enligt Vårdguidens rekommendationer behöver individer i din ålder ({ålder} år) sova minst {sömnbehov} timmar per natt.")


# uppgift 3.3
import random
dice = random.randint(1, 6)

if dice == 1:
    print("""
Du slog en 1:a!
---------
|       |
|   X   |
|       |
---------
  """)
elif dice == 2:
    print("""
Du slog en 2:a!        
---------
|      X|
|       |
| X     |
---------
""")
        
elif dice == 3:
    print("""
Du slog en 3:a!        
---------
|      X|
|   X   |
| X     |
---------
""")
elif dice == 4:
    print("""
Du slog en 4:a!        
---------
|X     X|
|       |
|X     X|
---------
""")
elif dice == 5:
    print("""
Du slog en 5:a!        
---------
|X     X|
|   X   |
|X     X|
---------
""")
elif dice == 6:
    print("""
Du slog en 6:a!        
---------
|X     X|
|X     X|
|X     X|
---------
""")


#Uppgift 3.4
land = input("Skriv ett land: ")
land = land.capitalize()
lista_norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"]
lista_GB =["England", "Nordirland", "Skottland", "Wales"]

if land in lista_norden:
    print("Landet ligger i norden.")
elif land in lista_GB:
    print("Landet ligger i GB")
else:
    print("Landet ligger inte i norden eller GB")
'''


#Uppgift 3.5
kön = input("Skriv in ditt kön: ")
hårfärg = input("Skriv in din hårfärg: ")
ögonfärg = input("Skriv in din ögonfärg ")

if kön == "man":
    if hårfärg == "brun":
        if ögonfärg == "brun":
            print("Egenskaperna matchar med Daniel Radcliffe")
        elif ögonfärg == "grön":
            print("Egenskaperna matchar med Jhonny Depp")
        elif ögonfärg == "blå":
            print("Egenskaperna matchar med ingen")
        else:
            print("Egenskaperna matchar med ingen")

if kön == "kvinna":
    if hårfärg == "brun":
        if ögonfärg == "brun":
            print("Egenskaperna matchar med Emma Watson, Nathalie Portman och Selena Gomez")
        else:
            print("Egenskaperna matchar med ingen")









