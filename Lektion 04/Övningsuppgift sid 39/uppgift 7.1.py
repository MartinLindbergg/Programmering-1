# Anslagstavlan poster
POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    # Rensa terminalfönster
    print("\033c")

    # Skriv ut instruktioner och innehållet i anslagstavlan
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')

    # Hämta kommando från användaren
    choice = input('meny > ')

    if choice == 'c':
        # Låt användaren välja vilken post de vill ändra
        post_choice = input('Vilken post vill du ändra (P1/P2/P3)? ').upper()

        # Kolla vilken post användaren valt
        if post_choice == 'P1':
            POST_1 = input('Skriv den nya texten för P1: ')
        elif post_choice == 'P2':
            POST_2 = input('Skriv den nya texten för P2: ')
        elif post_choice == 'P3':
            POST_3 = input('Skriv den nya texten för P3: ')
        else:
            print('Ogiltigt val. Var vänlig och välj P1, P2 eller P3.')

    elif choice == 'e':
        # Avsluta programmet
        print('Programmet stängs av.')
        break

    else:
        print('Ogiltigt val. Var vänlig och välj c eller e.')

    # Pausa exekvering
    input('Tryck enter för att fortsätta ...')
