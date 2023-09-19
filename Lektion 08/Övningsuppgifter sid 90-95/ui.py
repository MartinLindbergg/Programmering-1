import os

def line(dots=False):
    # Skriver ut en serie bindestreck eller asterisker på skärmen
    if dots:
        print(30 * '*')
    else:
        print(30 * '-')

def header(text):
    # Skriver ut en rubrik på skärmen
    width = os.get_terminal_size().columns
    text = text.center(width)
    print(f"| {text} |")

def echo(text):
    # Skriver ut en text på skärmen
    width = os.get_terminal_size().columns
    text = text.center(width)
    print(f"| {text} |")

def prompt(text):
    # Hämtar input från användaren
    width = os.get_terminal_size().columns
    text = text.center(width)
    print(f"| {text} > ", end="")
    return input()

def clear():
    # Rensar skärmen
    os.system("clear")