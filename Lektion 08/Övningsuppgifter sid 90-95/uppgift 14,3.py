import random

# Utgå från sen lista med 10st random heltal
numbers = []
for x in range(10):
    numbers.append(random.randint(0, 9))

#Returnerar samtliga jämna heltal från listan numbers
def get_even(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even

even = get_even(numbers)
print("Jämna tal i listan:", even)
print("Alla tal i listan:", numbers)
