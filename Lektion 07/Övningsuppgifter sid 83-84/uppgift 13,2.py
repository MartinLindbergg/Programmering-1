import requests

try:
    city = input("Ange namnet på staden för väderprognoser: ").strip().lower()
    # URL för väder-API:et
    base_url = (f"https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{city}")
    # Kontrollera om staden är giltig
    valid_cities = ["stockholm", "goteborg", "malmo", "uppsala", "vasteras"]
    if city not in valid_cities:
        print("Ogiltig stad. Vänligen ange en av följande städer: Stockholm, Göteborg, Malmö, Uppsala, Västerås")
    else:
        # Gör ett API-anrop för att hämta väderprognoser för den angivna staden
        response = requests.get(base_url + city)

        if response.status_code == 200:
            data = response.json()
            forecasts = data.get("forecasts", [])

            print("----------------------")
            print("FORECASTS")
            print("********************")

            for forecast in forecasts:
                date = forecast.get("date", "")
                weather = forecast.get("weather", "")
                print(f"{date} {weather}")

            print("----------------------")
        else:
            print("Kunde inte hämta väderprognoser för staden.")
except Exception as e:
    print("Ett fel uppstod:", str(e))
