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

