# Funktion för att läsa in persondata från filen och returnera en lista av dictionarys
def load_people_data(filename):
    people_data = []
    with open(filename, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            person = {}
            for i, key in enumerate(header):
                person[key.strip()] = values[i].strip()
            people_data.append(person)
    return people_data

# Funktion för att söka och skriva ut information om en person baserat på ID
def get_person_by_id(people_data, person_id):
    for person in people_data:
        if person['ID'] == person_id:
            print_person_info(person)
            return
    print("Person not found!")

# Funktion för att skriva ut information om en person
def print_person_info(person):
    print("ID:", person['ID'])
    print("First Name:", person['FORENAME'])
    print("Last Name:", person['SURNAME'])
    print("Gender:", person['GENDER'])
    print("Year of Birth:", person['YEAR'])
    print()

# Funktion för att lista personer med matchande förnamn
def list_people_by_forename(people_data, forename):
    matching_people = [person for person in people_data if person['FORENAME'].lower() == forename.lower()]
    if matching_people:
        for person in matching_people:
            print_person_info(person)
    else:
        print("No matching people found!")

# Funktion för att lista personer med matchande efternamn
def list_people_by_surname(people_data, surname):
    matching_people = [person for person in people_data if person['SURNAME'].lower() == surname.lower()]
    if matching_people:
        for person in matching_people:
            print_person_info(person)
    else:
        print("No matching people found!")

# Huvudprogram
if __name__ == "__main__":
    filename = "people_data.txt"
    people_data = load_people_data(filename)
    
    print(".: PEOPLES DATABASE :.")
    print("----------------------")
    print("get_id | Get person by ID")
    print("scan_f | List people by FORENAME")
    print("scan_s | List people by SURNAME")
    print("exit   | Exit program")
    print("----------------------")

    while True:
        choice = input("| > ").strip()
        
        if choice == "get_id":
            person_id = input("Enter ID: ")
            get_person_by_id(people_data, person_id)
        elif choice == "scan_f":
            forename = input("Enter FORENAME: ")
            list_people_by_forename(people_data, forename)
        elif choice == "scan_s":
            surname = input("Enter SURNAME: ")
            list_people_by_surname(people_data, surname)
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please try again.")
