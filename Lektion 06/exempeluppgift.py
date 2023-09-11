person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name":"Morris", "age": 3, "type": "Hund"},
        {"name": "Lisa", "age": 3, "type": "Katt"}
    ]
}

name = person["firstname"] + " " + person["lastname"]
age = person["age"]
pets = person["pets"]
count_pets = len(person["pets"])


print(f"{name} är {age} år gammal och har {count_pets} husdjur:")

for pet in pets:
    print(f"* En {pet['age']} år gammal {pet['type']} som heter {pet['name']}")