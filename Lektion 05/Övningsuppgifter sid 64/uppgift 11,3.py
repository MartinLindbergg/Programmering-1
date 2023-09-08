'''
För att implementera ett interaktivt Python-script där användaren kan mata in en serie heltal,
och scriptet memoriserar endast unika heltal samt visar summan av dem, kan du använda en fil för
att lagra de tidigare inmatade heltalen. Här är ett exempel på ett sådant
script:'''

import os

# Funktion för att läsa tidigare heltal från en fil
def load_numbers(filename):
    if not os.path.exists(filename):
        return set()
    with open(filename, 'r') as file:
        numbers = set(map(int, file.read().split()))
    return numbers

# Funktion för att spara heltal till en fil
def save_numbers(filename, numbers):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, numbers)))

# Huvudprogram
filename = "memorized_numbers.txt"
numbers = load_numbers(filename)

print(".: intMEMORIZER :.")
print("******************")

while True:
    print("Mata in heltal")
    print("0 stänger scriptet")
    print("------------------")

    try:
        input_number = int(input("> "))
        
        if input_number == 0:
            break
        
        if input_number not in numbers:
            numbers.add(input_number)
        
        total_sum = sum(numbers)
        
        print("------------------")
        for num in numbers:
            print(f"* {num}")
        print("------------------")
        print(f"SUMMA : {total_sum}")
        print("------------------")
        
        save_numbers(filename, numbers)
    except ValueError:
        print("Ogiltigt heltal. Försök igen.")

print("Scriptet har stängts.")

