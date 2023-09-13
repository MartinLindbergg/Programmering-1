
# Skapa dictionary med anteckningar
notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

# Iterera över dictionaryt och skriv ut titel och text för varje anteckning
for rubrik, text in notes.items():
    print("-----")
    print("Titel:", rubrik)
    print("Text:", text)




'''
Metoden .items() används i en dictionary för att hämta en lista av tuplar,
där varje tupel består av en nyckel och dess motsvarande värde från dictionaryt.
'''
