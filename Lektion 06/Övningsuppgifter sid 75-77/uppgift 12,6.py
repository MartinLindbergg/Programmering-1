import json

# Funktion för att läsa data från en JSON-fil
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = {}
    return notes

# Funktion för att spara data till en JSON-fil
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# Funktion för att visa all data
def view_notes(notes):
    for title in notes:
        print(f"- {title}")

# Funktion för att visa en specifik anteckning
def view_note(notes, title):
    if title in notes:
        print(f"Title: {title}")
        print(f"Text: {notes[title]}")
    else:
        print("Anteckningen hittades inte.")

# Funktion för att lägga till en ny anteckning
def add_note(notes, title, text):
    notes[title] = text
    print(f"Anteckningen '{title}' har lagts till.")

# Funktion för att ta bort en anteckning
def remove_note(notes, title):
    if title in notes:
        del notes[title]
        print(f"Anteckningen '{title}' har tagits bort.")
    else:
        print("Anteckningen hittades inte.")

# Huvudprogram, skapar en kodblock som endast körs om skriptet körs som huvudprogram 
if __name__ == "__main__":
    notes = load_notes()
    
    while True:
        print("------------------")
        print(".: ALWAYSNOTE :.")
        print("-- gold edition --")
        print("******************")

        view_notes(notes)

        print("------------------")
        print("view | view note")
        print("add | add note")
        print("rm | remove note")
        print("exit | exit program")
        print("------------------")
        choice = input("menu > ").strip()

        if choice == "view":
            title = input("Ange titel för att visa: ").strip()
            view_note(notes, title)
        elif choice == "add":
            title = input("Ange titel: ").strip()
            text = input("Ange text: ").strip()
            add_note(notes, title, text)
            save_notes(notes)
        elif choice == "rm":
            title = input("Ange titel att ta bort: ").strip()
            remove_note(notes, title)
            save_notes(notes)
        elif choice == "exit":
            break







'''
Detta program använder en JSON-fil (notes.json) för att spara och ladda anteckningar.
Man kan använda detta program för att visa, lägga till, ta bort och hantera personliga anteckningar.
Anteckningarna kommer att sparas mellan körningar, och man kan avsluta programmet när man är klar.
'''