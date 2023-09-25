# En klass kan man säga är tex ett Djur

#Djur
#   Art           Hund
#   Namn          Bosse
#   Antal ben     4
#   Kan flyga?    False



#Class (en mall som kan användas vid alla objekt)
class Djur():                                   
    #Konstruktor (self-parametern)
    #Används vid instansering
    def __init__(self):
        self.art = "Ingen art"
        self.namn = "Inget namn"
        self.ben = 0
        self.kan_flyga = False
    
    #Metoder (En metod som printar ut information om objektet)
    def print_djur(self):
        print("Information om objektet (Djur)")
        print("\tArt:", self.art)
        print("\tNamn:", self.namn)
        print("\tAntal ben:", self.ben)
        
        if self.kan_flyga == True:
            print("\tKan flyga")
        else:
            print("\tKan inte flyga")

class Zoo():
    #konstruktor
    def __init__(self):
        self.djur_lista = []
        self.namn = "Inget namn"
    #Metoder
    #Lägger till ett djur
    def lägg_till_djur(self, nytt_djur):
        #parameter nytt_djur är ett Djur-objekt
        self.djur_lista.append(nytt_djur)

    #Ger antalet djur i zooet
    def print_zoo(self):
        return len(self.djur_lista)
    
    #Skriv ut info om alla djur
    def print_zoo(self):
        print("Zoonamn:", self.namn)
        print("Antal djur:", self.antal_djur())

    #Ta bort ett djur med angivet namn
    def ta_bort_djur(self, djur_namn):
        #parameter djur_namn str
        ta_bort_index = -1
        for djur_index in range(0, self.antal_djur()):
            if self.djur_lista[djur_index].namn == djur_namn:
                ta_bort_index = djur_index
        self.djur_lista.pop(ta_bort_index)



#Instansiera ett objekt av klassen Djur
apa = Djur()
apa.art = "Apa"
apa.namn = "Nicke Nyfiken"
apa.ben = 2
apa.print_djur()

hund = Djur()
hund.art = "Hund"
hund.namn = "Pluto"
hund.ben = 4
hund.print_djur()

skata = Djur()
skata.art = "Skata"
skata.namn = "Krax"
skata.ben = 2
skata.kan_flyga = True
skata.print_djur()

nytt_zoo = Zoo()
nytt_zoo.namn = "Nya Zooet"
nytt_zoo.lägg_til_djur(skata)
