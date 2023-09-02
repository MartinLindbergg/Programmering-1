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