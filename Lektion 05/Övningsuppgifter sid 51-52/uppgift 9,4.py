#Uppgifter i en lista
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
#UI
ui_width = 30
#Printar ut ui och centrerar
print("TO DO LIST".center(ui_width))
print(ui_width * "-")

#funktion
for syssla in todos:
    print("-",syssla,"-")