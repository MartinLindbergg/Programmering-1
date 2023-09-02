# uppgift 4.1
biggest_number = float('-inf')
smallest_number = float('inf')


while True:
    user_input = input("Mata in ett tal: ")
    user_input = int(user_input)
    if int(user_input) < 0:
        break
    number_of_numbers =+ 1
    sum =+ user_input
    if user_input < smallest_number:
        smallest_number = user_input
    if user_input > biggest_number:
        biggest_number = user_input
if number_of_numbers > 0:
    average = sum / number_of_numbers
else: average = 0

print("Största tal är: ", biggest_number)
print("Minsta tal är: ", smallest_number)
print("Medelvärdet är: ", average)
