print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


# The backslash helps us to ignore the nested "" and ''
left_or_right = (input("You're at a cross road, You have two paths \"Left\" or \"Right\". Which way do u go? ")).lower()
if (left_or_right == "left"):
    swim_or_wait = (input("You found an lake. do you Swim or wait? ")).lower()
    if(swim_or_wait == "wait"):
        door = (input("There is a blue, a red and a yellow door. Which one do you choose? ")).lower()
        if(door == "blue"):
            print("There was fire behind the door, you were burned alive, Game Over")
        elif(door == "red"):
            print("There was a bear behind the door, he clawed you to death, Game Over")
        elif(door == "yellow"):
            print("You have reached vinland, You Win")
        else:
            print("You chose a door that doesn't exist, Game Over")
    else:
        print("There was a crocodile in the lake, You Died, Game Over")
else:
    print("You fell into a hole, You Died, Game Over")


