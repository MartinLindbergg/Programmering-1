# Öppna filen med heltalen
with open('EnMiljonHeltal.txt', 'r') as file:
    data = file.read()

# Skapa en lista med antalet förekomster av varje heltal
count = [0] * 10
for digit in data:
    if digit.isdigit():
        count[int(digit)] += 1

# Skriv ut resultatet
print("- NUMANALYZER -")
print("----------------")
for numbers in range(10):
    print(f"| {numbers} | {count[numbers]}")
print("----------------")

