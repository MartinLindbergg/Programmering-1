import random

def word_guessing_game():

  # Ord som kan vara korrekt
  tema_1 = random.choice(["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar",
                        "musmatta", "lampa", "bildskärm", "laddstation", "musmatta"])

  # Skapa en lista med bokstäver som spelaren har gissat.
  guessed_letters = []

  # Spela spelet.
  while True:
    # Be spelaren att gissa ett ord.
    guessed_letter = input("Gissa ett ord: ")

    # Kontrollera om spelaren gissade rätt.
    if guessed_letter == tema_1:
      # Spelaren vann!
      print("Grattis, du gissade rätt!")
      break

    # Om spelaren inte gissade rätt, lägg till den gissade bokstaven till listan med gissade bokstäver.
    guessed_letters.append(guessed_letter)

    # Visa spelaren hur många bokstäver de har gissat rätt.
    print("Du har gissat rätt på följande bokstäver:", ", ".join(guessed_letters))

    # Om spelaren har förbrukat alla sina gissningar, avsluta spelet.
    if len(guessed_letters) == len(tema_1):
      print("Du förlorade! Det rätta ordet var", tema_1)
      break

if __name__ == "__main__":
  word_guessing_game()
