while True:
    try:
        a = float(input("Skriv in värdet för a: "))
        0 / a
        break
    except ValueError:
        print("\nFEL: Ogiltigt nummer. Försök igen.\n")
    except ZeroDivisionError:
        print("\nFEL: Division med 0 är inte tillåten. Försök igen.\n")

while True:
    try:
        b = float(input("Skriv in värdet för b: "))
        a / b
        break
    except ValueError:
        print("\nFEL: Ogiltigt nummer. Försök igen.\n")
    except ZeroDivisionError:
        print("\nFEL: Division med 0 är inte tillåten. Försök igen.\n")

result = a / b

print("\n********************")
print("* The Great Divider *")
print("---------------------")
print("a =", a)
print("b =", b)
print("---------------------")
print("Resultat: ", a, "/", b, "=", result)

