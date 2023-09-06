#Funktion för a-värdet
while True:
    try: #skriv in ett värde för a, om 0 mats in körs programmet om
        a = float(input("Skriv in värdet för a: "))
        0 / a
        break
    #Felhantering, om användare skriver in något annat än ett tal
    except ValueError:
        print("\nFEL: Ogiltigt nummer. Försök igen.\n")
    #Felhantering, om användaren skriver in 0
    except ZeroDivisionError:
        print("\nFEL: Division med 0 är inte tillåten. Försök igen.\n")
#Funktion för b-värdet (samma som a-värdet)
while True:
    try:
        b = float(input("Skriv in värdet för b: "))
        a / b
        break
    except ValueError:
        print("\nFEL: Ogiltigt nummer. Försök igen.\n")
    except ZeroDivisionError:
        print("\nFEL: Division med 0 är inte tillåten. Försök igen.\n")
#delar det inmatade a-värdet med det inmatade b-värdet
result = a / b
#ui som printar du a-värdet och b-värdet samt resultat av a delat på b.
print("\n********************")
print("* The Great Divider *")
print("---------------------")
print("a =", a)
print("b =", b)
print("---------------------")
print("Resultat: ", a, "/", b, "=", result)

