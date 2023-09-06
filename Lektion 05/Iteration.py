'''
i=0
while i < len(deltagare):
    print("Välkommen " + deltagare[i])
    deltagare.remove(deltagare[i])


deltagare = ["Lina","Gunilla", "Erik", "Carl"]
for namn in deltagare:
    print(f"Välkommen {namn}")
    del deltagare[1]

'''


# Skriv ut alla heltal utan att använda while

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for tal in number:
    print(tal)



