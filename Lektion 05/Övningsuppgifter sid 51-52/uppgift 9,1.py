
#9.1
total_sum = 0
for i in range(1000001):
    total_sum += i

print("Summan av alla heltal mellan 0 och 1 000 000 är:", total_sum)


odd_sum = 0
for i in range(501):  # Vi använder 501 eftersom det inkluderar 500 också
    if i % 2 != 0:  # Kontrollera om talet är udda genom att använda modulo-operatören
        odd_sum += i

print("Summan av alla udda heltal mellan 0 och 500 är:", odd_sum)
