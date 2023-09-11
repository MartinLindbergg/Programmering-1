
# Skapa en dictionary med anteckningar
notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

# Be användaren mata in chose_note
chose_note = input("Choose your note > ")

# Försök skriva ut anteckningen om den finns i dictionary
if chose_note in notes:
    print("-----")
    print(chose_note)
    print("-----")
    print(notes[chose_note])
else:
    print(f"FEL: {chose_note} finns inte")

