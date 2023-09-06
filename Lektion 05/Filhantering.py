'''
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''
'''
import os
if os.path.exists("textfil.txt"):
    #öppna en befintlig fil (a = öppnar en befintlig fil)
    f = open("textfil.txt", "a")
else:
    #om inte filen finns, skapas en fil (X = create)
    f = open("textfil.txt", "x")

f.write("Rad 1\n")
f.write("Rad 2\n")
f.write("Rad 3\n")

#öppna och läs filen (R = read)
with open("textfil.txt", "r") as f:
    text = f.read()
print(text)


#Ta bort fil 
import os
if os.path.exists("textfil.txt"):
    os.remove("textfil.txt")
else:
    print("The file does not exist")
'''

#text från chatGPT
import os

try:
    if os.path.exists("textfil.txt"):
        # Öppna en befintlig fil i append-läge
        with open("textfil.txt", "a") as f:
            f.write("Rad 1\n")
            f.write("Rad 2\n")
            f.write("Rad 3\n")
    else:
        # Skapa en ny fil om den inte finns
        with open("textfil.txt", "x") as f:
            f.write("Rad 1\n")
            f.write("Rad 2\n")
            f.write("Rad 3\n")

    # Öppna och läs filen
    with open("textfil.txt", "r") as f:
        text = f.read()
    print(text)
except Exception as e:
    print(f"Ett fel inträffade: {str(e)}")

