'''
#Exempel 1
counter = 1
while counter <= 10:
    print("counter")
    counter = counter + 2


#Exempel 2
while True:
  print("This program is running")
  goAgain = input("Go again (y/n)? ")
  if goAgain == "n":
   break
print("Aww, I was having a good time")


#Exempel 3
while True:
  color = input("Enter a color: ")
  if color == "red":
     break
  else:
   print("Cool color!")
   print("I don't like red")
'''

#Exempel 4
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
   print("Ahh! You're a genius, you've won")
  exit()
print("The game is over, you've failed!")