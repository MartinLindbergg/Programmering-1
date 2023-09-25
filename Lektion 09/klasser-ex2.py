
# Skapa en klass

class Rectangle:
    # Attribut
    height = 0
    width = 0

    # Metod
    def area(self):
        return self.height * self.width
    
     # Övning 1 (Ny metod)
    def perimeter(self):
        return 2 * (self.height + self.width)

    
# Skapa ett objekt
r1 = Rectangle()
r1.height = 5
r1.width = 10

# övning 2 (skapa två nya bojekt)
r2 = Rectangle()
r2.height = 10
r2.width = 20


# En konstruktor är en speciell metod i en klass som används för att skapa och initialisera nya objekt från klassen
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


# Skapa ett objekt med hjälp av konstruktorn

r1 = Rectangle(5,10)
print(r1.height)
print(r1.width)
print(r1.area())

# Inkapsling
''' Inkapsling är en princip som innebär att vissa attribut och metoder kan vara privata och inte direkt nås utanför klassen.
Detta hjälper till att skydda och isolera klassens inerna tillståd och beteenden
Attribut och metoder som föregås av dubbla understreck __ är privata. De är starkt skyddade och ska normalt sett inte nås
eller ändras utanför klassen.'''

# Inkapsling exempel
class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
#Här får vi attribut error eftersom objekten är inkapslade med hjälp av __
r1 = Rectangle(5, 10)
print(r1.__height)

# Setters och Getters

# Setter-metod
def set_height(self, height):
    self.__height = height

# Getter-metod
def get_height(self):
    return self.__height


# Säkra metoder
def set_length(self, height):
    if height > 0:
        self.__height = height
    else:
        print(" Felaktig höj. Höjd måste vara större än 0.")

        

