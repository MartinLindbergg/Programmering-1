'''
# uppgift 4.2
while True:
    try:
        multiplikationstabell = int(input("Ange multiplikationstabell (avsluta med 'nej'): "))
        if multiplikationstabell < 0:
            break
        
        for i in range(3):
            resultat = multiplikationstabell * (i + 1)
            print(resultat)
        
        fortsatt = input("Fortsätt? (ja/nej): ")
        if fortsatt.lower() != 'ja':
            break
    except ValueError:
        print("Ogiltig input. Försök igen.")

print("Programmet avslutat.")
'''

# Alternativ
multi = int(input("Ange multiplikationstabell > "))
tal = 0
while True:
    tal += multi
    print(tal)
    tal += multi
    print(tal)
    tal += multi
    print(tal)
    cont = input("Fortsätt? ")
    if cont == "ja":
        continue
    else:
        break