#Användare matar in sin text och vilken bokstav som ska räknas
imput_text = input("Write your text: ")
imput_letter = input("Choose letter: ")
#Här utgår vi från index är 0
i = 0
#Variabel som håller koll på den valda bokstaven
letter_counter = 0

#
while i < len(imput_text):

    if imput_text[i].lower() == imput_letter:
        letter_counter += 1
    #I flyttar indexen genom hela texten
    i += 1

print("The chosen letter occurs", + letter_counter, "times in your text")

