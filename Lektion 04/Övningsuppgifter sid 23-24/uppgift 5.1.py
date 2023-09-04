
indata = input ("Skriv in ett tal:")

try:
    indata = int(indata)
    times_2 = indata * 2
    print("Tal:" , indata)
    print("Resultat:", times_2)

except ValueError:
    print(indata , "kan inte översättas till ett heltal")






