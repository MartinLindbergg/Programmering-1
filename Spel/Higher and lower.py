
print("   .: HIGHER AND LOWER GAME :.   ")
print("-------------------------------- ")
print("Welcome to The Higher Lower Game.")
print("I will randomise a number between")
print("    0 and 99 Can you guess it?   ")
print("---------------------------------")

import random
numb = random.randint(0, 99)
tal = int(input("Your guess > "))
tries = 1
while True:
    if tal > numb:
        print("LOWER!")
        tries+=1
    elif tal < numb:
        print("HIGHER!")
        tries+=1
    else:
        break
    tal = int(input("Try again > "))

print("---------------------------------")
print(numb, "is correct!")
print("It took you", tries, "guesses.")
print("Good job!")