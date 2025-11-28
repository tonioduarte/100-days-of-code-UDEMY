print ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print(" Welcome to the treasure island!")
print("This will be quite a journey, so be ready.")
Landing = input("You Landed in the island, which site are u taking? Right or Left ")
if Landing == "right":
    Right = input(" you founded a strange plant, would you eat it? yes or no? ")
    if Right == "yes":
        print(" you died :( )")
    elif Right == "no":
        print(" you're safe! this was a poison plant...")
        Swin = input(" while looking around, you found a misterious lake, would you swin? yes or no ")
        if Swin == "no":
            print(" a anaconda eats you while you where thinking... :( )")
        elif Swin == "yes":
            Follow = (" you found a mermaid! you follow her or stay at the lake? follow or stay")
            if Follow == "follow":
                print("she takes you to the her secret lake! she want to share her riches with you! :)")
            elif Follow == "stay":
                print("you drowned... :( ")  
else: 
    Ninja = input("you found a sleeping ninja, would you wake him? yes or no ")
    if Ninja == "yes":
        Help = input(" He wakes up, and tells you his name is Jhon and he needs your help to save her wife... would you help? yes or no ")
        if Help == "yes":
            print(" you help him and he rewards you with glory :)")
        else:
            print(" he kills you... :( ")
    else:
        Fly = input(" you avoid him and go sleep near an ancient tree, when you wake up, a giant bird wants to take you a fly, you accept? yes or no ")
        if Fly == "yes":
            print(" you see how pretty is the island from the sky and then you pet the bird and together you explore the world! :)")
        else:
            print(" the bird kills you!..:(" )