# Skapa en tom stack som är en lista
stack = []

# Funktion för att skriva ut stacken
def print_stack():
    print(".: STACKMASTER v1.33.7 :.")
    print("------------------------------")
    for item in stack:
        print(f"- {item}")
    print("------------------------------")

# Huvudloop för interaktion med användaren
while True:
    print_stack()

    print("| MENU |")
    print("------------------------------")
    print("push | Push element to stack")
    print("pull | Pull element from stack")
    print("exit | Exit program")
    print("------------------------------")

    choice = input("MENU > ").lower()

    if choice == "push":
        element = input("Ange vad du vill lägga till i stacken: ")
        stack.append(element)
    elif choice == "pull":
        if stack:
            pulled_element = stack.pop()
            print(f"{pulled_element} har plockats bort från stacken.")
        else:
            print("Stacken är tom.")
    elif choice == "exit":
        break
    else:
        print("Ogiltigt val. Försök igen.")

print("Programmet avslutas.")
