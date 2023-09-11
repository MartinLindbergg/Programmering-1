# Definiera dictionary med befintliga anteckningar
notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

# Mata in titel och text för den nya anteckningen
new_title = input("Lägg till artikel:\ntitel > ")
new_text = input("text > ")

#Lägg till den nya anteckningen i dictionaryt(Här blir new_titel den nya nyckeln och new_text nya värdet)
notes[new_title] = new_text

# Skriv ut alla anteckningar med hjälp av en forloop

for titel, text in notes.items():
    print("-----")
    print("Titel :", titel)
    print("Text :", text)
    print("-----")


'''
Detta är en for-loop som itererar över dictionaryn med hjälp av .items()-metoden.
For-loopen kommer att hämta varje nyckel-värde-par (titel och text) från dictionaryn.
'''
