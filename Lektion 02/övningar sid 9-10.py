
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

prislista = {
    "Vanlig korv": 20.95,
    "Vegansk korv": 34.95,
    "Dryck": 13.95
}

def berakna_inkop_och_kostnad(elev_data):
    total_korvar = 0
    total_veganska_korvar = 0
    total_drycker = 0

    for elev in elev_data:
        korvar = [2 * elev[0], 3 * elev[1]]
        veganska_korvar = [2 * elev[2], 3 * elev[3]]

        total_korvar += sum(korvar)
        total_veganska_korvar += sum(veganska_korvar)
        total_drycker += elev[4]

    korvar_förpackningar = (total_korvar + total_veganska_korvar) / 8
    veganska_korvar_förpackningar = total_veganska_korvar / 4
    total_kostnad = (korvar_förpackningar * prislista["Vanlig korv"] + veganska_korvar_förpackningar * prislista["Vegansk korv"] + total_drycker * prislista["Dryck"])

    return korvar_förpackningar, veganska_korvar_förpackningar, total_drycker, total_kostnad

def mata_in_elevdata():
    antal_elever = int(input("Ange antal elever: "))
    elev_data = []

    for i in range(antal_elever):
        elev_input = [int(input(f"Antal elever som vill äta {j} {produkt} (elev {i + 1}): ")) for j, produkt in zip([2, 3, 2, 3, 1], ["vanliga korvar", "vanliga korvar", "veganska korvar", "veganska korvar", "drycker"])]
        elev_data.append(tuple(elev_input))

    return elev_data

if __name__ == "__main__":
    elev_data = mata_in_elevdata()
    korvar_förpackningar, veganska_korvar_förpackningar, total_drycker, total_kostnad = berakna_inkop_och_kostnad(elev_data)

    print(f"Antal förpackningar med vanliga korvar att köpa: {korvar_förpackningar:.2f}")
    print(f"Antal förpackningar med veganska korvar att köpa: {veganska_korvar_förpackningar:.2f}")
    print(f"Antal drycker att köpa: {total_drycker}")
    print(f"Total kostnad: {total_kostnad:.2f} kr")
