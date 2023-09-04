
#...:FÄRG-GISSAREN:...


import os
if os.name == "nt":
    os.system('cls')

elif os.name == "posix":
    os.system("clear")


ui_width = 30

#Ritar upp intro
print(ui_width * '*')
print('FÄRG-GISSAREN 2.0'.center(ui_width))
print(ui_width * '-')
print(':: REGLER ::'.center(ui_width))
print('Gissa en färg!'.center(ui_width))
print('Gissar du rätt färg'.center(ui_width))
print('vinner du spelet!'.center(ui_width))
print('-' * ui_width)

# Antal försök
times = 1

#Hämtar indata från användare
color = input('Gissa färg > ').lower()

#Kontrollerar inmatningen
while color != 'gul':
    print('Fel gissning , försök igen... ')
    times += 1
    color = input('Gissa färg > ').lower()

#Skriver ut resultat
print('-' * 23)
print('Korrekt gissat efter', times, 'försök!')
input("Tryck på retur för att spela igen")