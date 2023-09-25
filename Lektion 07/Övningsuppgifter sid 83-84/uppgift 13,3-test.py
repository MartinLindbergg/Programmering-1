import requests

def get_artist_list():
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        artists = data.get("artists", [])
        return artists
    else:
        return None

class Artist:
    def __init__(self, id, name, genres, years_active, members):
        self.id = id
        self.name = name
        self.genres = genres
        self.years_active = years_active
        self.members = members

    def __str__(self):
        return f"{self.name} ({self.genres})"

class ArtistDatabase:
    def __init__(self, url):
        self.url = url
        self.artists = []

    def get_artist_list(self):
        # Hämta listan över artister från API:et
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            artists = data.get("artists", [])
            return artists
        else:
            return None

    def get_artist_info(self, artist_id):
        # Hämta information om artisten från API:et
        url = f"{self.url}/{artist_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def find_artist_by_name(self, artist_name):
        for artist in self.artists:
            if artist_name in artist.name.lower():
                return artist

        return None

if __name__ == "__main__":
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artist_database = ArtistDatabase(url)

    # Hämta listan över artister
    artist_list = artist_database.get_artist_list()

    # Skriv ut listan över artister
    if artist_list:
        print("--- ARTIST DB ---")
        for artist in artist_list:
            print(artist)
        print("-----------------")

        # Användaren anger en artist att söka på
        artist_name = input("Select artist: ").strip().lower()

        # Hitta artisten med det angivna namnet i listan
        selected_artist = artist_database.find_artist_by_name(artist_name)

        if selected_artist:
            print("-----------------")
            print(selected_artist)
            print("*****************")

            # Hämta fördjupande information om den valda artisten
            artist_info = artist_database.get_artist_info(selected_artist.id)

            print(f"Genres: {', '.join(artist_info.genres)}")
            print(f"Years active: {artist_info.years_active}")
            print(f"Members: {artist_info.members}")
            print("-----------------")
        else:
            print(f"Artist '{artist_name}' hittades inte i listan.")
    else:
        print("Kunde inte hämta artistlistan från API:et.")
