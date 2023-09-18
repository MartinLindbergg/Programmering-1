import requests

# Funktion för att hämta en lista över tillgängliga artister
def get_artist_list():
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        artists = data.get("artists", [])
        return artists
    else:
        return None

# Funktion för att hämta fördjupande information om en artist
def get_artist_info(artist_id):
    url = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

try:
    artist_list = get_artist_list()
    if artist_list:
        print("--- ARTIST DB ---")
        for artist in artist_list:
            print(artist.get("name"))
        print("-----------------")

        artist_name = input("Select artist: ").strip().lower()

        # Hitta artisten med det angivna namnet i listan
        selected_artist = next((artist for artist in artist_list if artist_name in artist["name"].lower()), None)

        if selected_artist:
            print("-----------------")
            print(selected_artist["name"])
            print("*****************")

            # Hämta fördjupande information om den valda artisten
            artist_info = get_artist_info(selected_artist["id"])
            if artist_info:
                genres = ', '.join(artist_info.get("genres", []))
                years_active = artist_info.get("years_active", "")
                members = artist_info.get("members", "")

                print(f"Genres: {genres}")
                print(f"Years active: {years_active}")
                print(f"Members: {members}")
            else:
                print("Kunde inte hämta information om artisten.")
            print("-----------------")
        else:
            print(f"Artist '{artist_name}' hittades inte i listan.")
    else:
        print("Kunde inte hämta artistlistan från API:et.")
except Exception as e:
    print("Ett fel uppstod:", str(e))
