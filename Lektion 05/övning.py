
#Förklara vad som händer när detta program körs
attendants = ['Lisa','Kalle', 'Olivia', 'Johan']
with open('textfil.txt', 'w') as f:
    for attendant in attendants:
        f.write('Hello ' + attendant + '!\n')

#Svar: Programmet skapar en fil som heter textfile.txt med texten 
#Hello Lisa! 
#Hello Kalle!
#Hello Olivia!
#Hello Johan!
