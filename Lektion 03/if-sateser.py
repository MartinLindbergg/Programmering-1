
#Exempel 1

print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")

if username == "admin" and password == "pass123":
    print("Welcome")

else:
    print("Wrong Password!")



#Exempel 2

team = "engineering"

if team == "content":

  print("This person comes from the content team.")

elif team == "engineering":

  print("This person comes from the engineering team.")

else:
  print("This person doesn't come from the content or engineering teams.")


#Exempel 3

order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")

  else:
    print("No cheese it is.")

elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")

else:
  print("Your pizza will not have pepperoni.")