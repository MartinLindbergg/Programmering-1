#2.1
citat =" datatyper har inbyggda metoder "
print(citat.upper())


#2.2
tal = float(input("Ange ett decimaltal: "))
svar = tal
print(round(svar))


#2.3
print("Hallå")
fråga_1 = input("Vad är ditt förnamn? ")
fråga_2 = input("Vad är ditt efternman?")
print("Trevligt att träffa dig", fråga_1 , fråga_2)


#2.4
ålder = int(input("Hur gammal är du?"))
år_till_myndig = 18 - ålder
if år_till_myndig > 0:
    print(f"Du uppnår mynding ålder om {år_till_myndig} år.")


#2.5
heltal_lista = []
for i in range(5):
    hel_tal = int(input(f"Mata in totalt fem heltal #{i + 1}: "))
    heltal_lista.append(hel_tal)
högsta_tal = max(heltal_lista)
print(f"Det högsta talet du matade in är: {högsta_tal}")

#2.6
