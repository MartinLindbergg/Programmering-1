# Importera Tkinter-modulen för att skapa GUI-applikationer och random-modulen för slumpmässig spelarval.
from tkinter import *
import random

# Funktionen som kallas när en spelare klickar på en knapp för att göra sitt drag.
def next_turn(row, column):
    global player

    # Kontrollera om knappen är tom och om det inte finns någon vinnare än.
    if buttons[row][column]['text'] == "" and check_winner() is None:
        buttons[row][column]["text"] = player

        # Byt spelare och uppdatera meddelandet i etiketten.
        if check_winner() is None:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")
        
        # Om det blir en oavgjord match, visa ett meddelande att det har blivit lika.
        elif check_winner() == "Tie":
            label.config(text="Tie")
        
        # Om det finns en vinnare, visa ett meddelande om vem som vunnit 
        # Markera de vinnande knapparna med grönt.
        else:
            label.config(text=check_winner() + " wins")

# Funktionen som kontrollerar om det finns en vinnare eller om matchen är oavgjord.
def check_winner():

    # Kolla rader och kolumner för att hitta en vinnare och markera de vinnande knapparna med grönt.
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return buttons[row][0]['text']
        
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return buttons[0][column]['text']

    # Kolla diagonala linjer för att hitta en vinnare och markera de vinnande knapparna med grönt.
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return buttons[0][0]['text']
    
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return buttons[0][2]['text']
    
    # Om ingen vinnare och inga tomma rutor återstår, är det en oavgjord match
    # Markera alla knappar med rött.
    elif not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Tie"
    
    return None

# Funktionen som kollar om det finns tomma rutor kvar på spelbrädet.
def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

# Funktionen som startar en ny spelomgång och resetar spelet.
def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Skapa ett fönster för spelet.
window = Tk()
window.title("Tic-Tac-Toe")

# Välj vilken symbol du vill spela som och slumpa startspelaren.
players = ["O", "X"]
player = random.choice(players)

# Skapa en label för att visa spelarinformation.
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Skapa en knapp för att starta en ny omgång.
reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Skapa en ram för att innehålla spelet.
frame = Frame(window)
frame.pack()

# Skapa en matris av knappar som representerar spelet.
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, 
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Starta huvudloopen för spelet.
window.mainloop()
