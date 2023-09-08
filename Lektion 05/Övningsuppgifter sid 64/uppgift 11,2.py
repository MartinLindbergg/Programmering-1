'''
För att omvandla den JSON-formaterade strängen my_chars till en lista i Python och sedan
skriva ut varje objekt på en ny rad kan du använda json-biblioteket.
'''

import json

# Ange den JSON-formaterade strängen
my_chars = '[" abc" , "\u00e5\u00e4\u00f6 " , "123"]'

# Omvandla JSON-strängen till en Python-lista
char_list = json.loads(my_chars)

# Skriv ut varje objekt på en ny rad genom att iterera listan
for item in char_list:
    print(item.strip())  # Använd strip() för att ta bort onödig mellanslag


'''
I detta script använder vi json.loads för att omvandla den JSON-formaterade strängen my_chars till en
Python-lista. Sedan använder vi en enkel for-loop för att iterera över listan och skriva ut varje
objekt på en ny rad, använda strip() för att ta bort eventuella onödiga mellanslag runt objekten.

När du kör detta script kommer det att skriva ut varje objekt i listan på separata rader, som du önskade.

'''