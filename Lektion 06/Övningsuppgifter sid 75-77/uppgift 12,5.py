# Definiera dictionary med befintliga anteckningar
notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

# Be användaren mata in titel för den anteckning som ska tas bort
remove = input("Ta bort artikel: ")

# Tar bort anteckningen om den finns, annars skriv ut ett felmeddelande
if remove in notes:
    removed_item = notes.pop(remove)
    print("Artiklar kvar:")
    print("-----")

else:
    print(f"FEL: {remove} finns inte")

# Skriv ut samtliga återstående anteckningar (samma forloop som uppgift 12,4.py)
for titel, text in notes.items():
    print("Titel :", titel)
    print("Text :", text)
    print("-----")


'''
Här matar vi in titeln för den anteckning som ska tas bort.
Sedan använder vi .pop(remove) för att ta bort den angivna anteckningen från dictionaryt. 
'''