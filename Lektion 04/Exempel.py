# Hantering av felkod
'''Om vi skriver fem istället för 5 när programmet körs får vi ett felmeddelande. I detta fall får
vi även varför vi får felmeddelandet eftersom vi har gjort en print-funktion med except ValueError'''

#exempel 1
tal = input("Ange ett heltal:")
try:
  tal = int(tal)
  kvadrat = tal * tal
  print(tal, "i kvadrat är" , kvadrat)
except ValueError:
  print(tal , "är inte ett heltal")
