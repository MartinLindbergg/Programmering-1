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
