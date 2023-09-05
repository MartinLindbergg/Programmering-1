
konsonanter = "bcdfghjklmnpqrstvwxyz"
resultat = ""

text = input("Ange texten du vill översätta till rövarspråket")

for b in text:
    if b.lower() in konsonanter:
        resultat += b + "o" + b
    else:
        resultat += b

print("Översättning till rövarspråket: ", resultat )







#Alternativ 2
'''
def translate_to_robber(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = ""

    for letter in text:
        if letter.lower() in consonants:
            result += letter + "o" + letter
        else:
            result += letter
    
    return result

text = input("Ange texten du vill översätta till rövarspråket: ")

translated_text = translate_to_robber(text)
print("Din översättning till rövarspråket:", translated_text)
'''

