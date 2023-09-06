
def is_palindrome(text):
    text = text.lower().replace(" ","") # Konvertera till gemener och ta bort mellanslag
    return text == text[::-1]       # Compare text to its reversed version

input_str = input("Input string: ") # user string

if is_palindrome(input_str):
    print(" It's a Palindrom.")
else:
    print("It's not a palindrome.")





#Alternativ
'''
#Användaren skriver in en text
input_str = input("Ange en text: ")
#Tar bort blanksteg och skiljetecken och konvertera till små bokstäver
cleaned_str = ''.join(filter(str.isalnum, input_str)).lower()

#Jämför strängen med dess omvända form
if cleaned_str == cleaned_str[::-1]:
    print(input_str, "är ett palindrom")
else:
    print(input_str, "är inte ett palindrom")
'''







# Alternativ
'''
def is_palindrom(input_str):
    cleaned_str = ''.join(filter(str.isalnum, input_str)).lower()

    return cleaned_str == cleaned_str[::-1]

input_str = input("Ange en text: ")

if is_palindrom(input_str):
    print(input_str, "är en palidrom")
else:
    print(input_str, "är inte ett palindrom")
'''