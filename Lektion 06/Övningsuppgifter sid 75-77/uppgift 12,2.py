
# Skapa en dictionary med anteckningar
notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

# Skriv ut rubrik för anteckningarna med hjälp av en for loop
print(".: ANTECKNINGAR :.")
print("******************")

for heading in notes.keys():
    print("-", heading)

print("------------------")


'''
Metoden .keys() används med en dictionary för att hämta en lista över alla nycklar (keys)
som finns i det dictionaryt.
'''