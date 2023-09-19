# Funktion för att konvertera kilometer till miles
def km_to_miles(dist):
    miles = dist * 0.621371
    return miles

# Tvärtom
def miles_to_km(dist):
    km = dist / 0.621371
    return km

# Huvudprogram
while True:
    try:
        input_value = float(input("Välj distans: "))
        
        # Kolla om km finns med i input
        if "km" in input("Beräkna km eller miles?: ").lower():
            converted_dist = km_to_miles(input_value)
            print(f"{input_value} km motsvarar {converted_dist} miles.")
        
        # Om inte km finns med i input
        else:
            converted_dist = miles_to_km(input_value)
            print(f"{input_value} miles motsvarar {converted_dist} km.")
        
        break
    except ValueError:
        print("Felaktig inmatning. Försök igen.")

