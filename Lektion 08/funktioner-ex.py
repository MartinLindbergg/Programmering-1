'''
def funktionsnamn(parametrar):
    # Funktionskropp


def addera(tal_1, tal_2):
    summa = tal_1 + tal_2
    return summa

#Anropa en fuktion (call / invoke)

result = addera(1, 2)
result = addera(8, 3)

#printa ut

print(result)


    

def minimun(numbers):
    # Kontrollera om listan är tom
    if len(numbers) == 0:
        return None  # Returnera None om listan är tom

    # Initiera det minsta talet med det första elementet i listan
    min_number = numbers[0]

    # Loopa igenom resten av elementen i listan
    for number in numbers:
        # Jämför det nuvarande elementet med det minsta hittills
        if number < min_number:
            min_number = number

    return min_number

# Exempel på hur du kan använda funktionen
numbers = [5, 2, 7, 4, 9]
print(minimun(numbers))  # Detta kommer att skriva ut det minsta talet (2) från listan


#Övning returnera det minsta talet i listan.

def minimum(lista):
    lowest_number = lista[0]
    for i in lista:
        if(lowest_number > i):
            lowest_number = i

    return lowest_number

#kiss (Keep It Simple, Stupid)

def minimum (lista):
    return min(lista)

numbers = [5, 2, 7, 4, 9]

print(minimum(numbers))



#Exempel på funktion med flera argument

def greet (first_name , last_name):                               # Definera greet
    print("Hej", first_name , last_name, "Välkommen")             # Printa ut greet

greet("Martin","Lindberg")                                        # Skriv direkt i greet funktionen





# Funktionen sum()

# Sortera en lista i stigande ordning

lista = [5, 2, 9, 1, 5]
sorted_lista = sorted(lista)
print(sorted_lista)


# Sortera en lista av strängar
lista = ['c', 'beef', 'abba', 'b', 'a', 'cafe']
sorted_lista = sorted(lista)
print(sorted_lista)
'''


# Sortera en dictionary

fotboll = [
{'country': 'Russia', 'points': 3},
{'country': 'Brazil', 'points': 7},
{'country': 'Cameroon', 'points': 1},
{'country': 'Sweden', 'points': 5}
]


def get_points(element):
    return element['points']

fotboll = sorted(fotboll, key=get_points, reverse=True)

print(fotboll)