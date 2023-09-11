'''
#Exempel

# Skapa en dictionary
person_info = {
    'namn': 'Alice',
    'ålder': 30,
    'yrke': 'Ingenjör'
}

# Hämta värden från dictionary med hjälp av nycklar
print(person_info['namn'])  # Skriver ut 'Alice'
print(person_info['ålder'])  # Skriver ut 30
print(person_info['yrke'])   # Skriver ut 'Ingenjör'

# Lägg till ett nytt nyckel-värde-par
person_info['stad'] = 'Stockholm'

# Uppdatera ett värde genom att använda nyckeln
person_info['ålder'] = 31

# Ta bort ett nyckel-värde-par
del person_info['yrke']

# Kolla om en nyckel finns i dictionary
if 'ålder' in person_info:
    print("Ålder finns i dictionary.")

# Iterera genom nyckel-värde-paren i dictionary
for nyckel, värde in person_info.items():
    print(f"{nyckel}: {värde}")
'''


#exempel 2
#Dictionary = ett objekt
#Skapa en ny dictionary
person = {
    "name":"Martin",
    "age":29
}

#Hämta ett element
'''
print("Hej " + person["name"])
print("Du är " + str(person["age"]) + " år gammal")
#kan också skrivas ut med hjälp av f-strings
print(f"Du är { person['age'] } år gammal")



attr = input("Ange attribut (nyckel) > ")

try:
    print(person[attr])
except KeyError as fel:
    print("Fel! Attributet existerar inte!")
    print("Du skrev: " + str(fel) + " vilket inte existerar")


# Ändra värdet (elementet)
person["age"] = 51

# Lägg till ny data (key och value) / element
person["adress"] = "Okänd"


# Ta bort data (key och value) / element
del person["age"]
print(person)


#Kopiera dict
temp = person
person["temp"] = "temp"
print(temp)


person_copy = person.copy()
person_copy["temp2"] = "temp2"


#interation av dicy
for key in person:
    print("Key:", key)
    print("value:", person[key])
'''

#nästlade dict

person["adress"] = {
    "gatuadress": "Testvägen",
    "ort": "Spånga",
    "postnummer": "1337"

}

#skriv ut adressen enligt svensk standard
print(person["adress"]["gatuadress"])
print(person["adress"]["postnummer"], person["adress"]["ort"])
