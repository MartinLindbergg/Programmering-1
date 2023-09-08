# Funktion för att skriva ut vägskylten med det aktuella meddelandet
def print_sign(message):
    border = "|-----------------------------------|"
    print(border)
    print("|-----------------------------------|")
    print(f"|     || Welcome to {message} ||    |")
    print("|-----------------------------------|")
    print(border)
    print("| C | Change sign message           |")
    print("| E | Exit program                  |")
    print("|-----------------------------------|")
    print("| >")

# Läs in det aktuella meddelandet från filen sign.txt om den finns
try:
    with open("sign.txt", "r") as file:
        current_message = file.read().strip()
except FileNotFoundError:
    current_message = "hej"

# Visa vägskylten med det aktuella meddelandet
print_sign(current_message)

# Huvudloop för interaktion med användaren
while True:
    choice = input().strip().lower()

    if choice == "c":
        new_message = input("Ange det nya meddelandet: ")
        # Uppdatera meddelandet och skriv det till filen sign.txt
        with open("sign.txt", "w") as file:
            file.write(new_message)
        print_sign(new_message)
    elif choice == "e":
        print("Programmet avslutas.")
        break
    else:
        print("Ogiltigt val. Försök igen.")









'''
    with open("sign.txt", "r")as forcenterx:
        #F orcenterx är hälften av alla mellanslag som får plats i skylten (18) minus hälften av antal bokstäver i meddelandet. omringar man meddelandet med varsin av denna variabel så centrerar det positionen utan att förstöra gränssnittet
        forcenterx = (18 - (len(forcenterx.read()))/2)
        # För säkerhetsskull så gör jag 2 variablar av forcenterx som nedan. skulle då forcenterx vara ett udda tal så blir forcenterspace1 ett mellanslag mindre än forcenterspace2. är talet uddan så hamnar meddelandet NÄSTAN i mitten men gränssnittets omgivning bibehålls
        forcenterspace1 = (" " * (math.floor(forcenterx)))
        forcenterspace2 = (" " * (math.ceil(forcenterx)))
        
        '''