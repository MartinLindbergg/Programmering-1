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
    current_message = "Västerås"

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
