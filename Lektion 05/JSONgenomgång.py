'''
• JSON (JavaScript Object Notation) är en textbaserad
datautbytesformat som används för att representera datastrukturer
och överföra data mellan datorer.
• JSON är lättläst för människor och lätt parsad och genererad av
datorprogram.
• JSON används ofta för att överföra data över nätverk, lagra
inställningar och konfigurationer, och spara data i filer. 
'''

import json
attendants = ["Åsa", "Kalle", "Olivia", "Johan"]

with open("data.json", "w") as myFile:
    myFile.write(json.dumps(attendants))

print(myFile[0])