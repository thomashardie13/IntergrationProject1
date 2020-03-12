# Intergration Project: Thomas Hardie: Text Based Adventure Game "Nerve"

#StartupCode
from time import sleep
print("Please enter a name for your character")
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.02)
line_1 = "Welcome to The Journey! This is a text based adventure game in which you will face many challenges, in order to beat the game, you shall navigate the challenges without death."
print_slow(line_1)



name = input()
print("Well then, " + name + "!")
print("Please enter the age of your character")
age = int(input())
if age >= 18:
    print("Your character is old enough to play.")
else:
    print("Yikes youngling, lets see how long a child like you will last in Nerve")
# age = age * 2 // 2 + 40 - 20 - 20 exhibits knowledge of operators
print(age)
lives = int(input("What is the number that correlates to the present month?: "))
if lives == 9 or lives == 4 or lives == 6 or lives == 11:
  print("You have 30 minutes for 30 days of that month")
elif lives == 1 or lives == 3 or lives == 5 or lives == 7 or lives == 12 or lives == 10 or lives == 8:
  print("You have 31 minutes for 31 days of that month")
elif lives == 2:
  print("You have 28 minutes for 28 days of that month")
print("I hope you are ready for what lies ahead, the control option will be stated when faced with a question, choose which option is best fit for your travel in your belief and see how long you can last in Nerve. Good Luck")
print(" Nerve sequence beginning...")
#BeginningNerveGame
print("You awake in a forest laying against a tall oak tree. You currently face dehydration, your mouth is dry, head is pounding and have no recollection of how you got there.")
print("You look around you and see nothing but trees, you hear what seems like a river nearby.")
print("Do you choose to go towards the river? Or do you stay and succumb to inevitable fate of death?")
print("Type Yes to move toward river. Type No to stay and die")
choice_1 = input()
if choice_1 == "Yes":
    print("You stand on your feet and begin towards the distant sound of running water")
else:
    print("You lay back again against the tree, you hear someone walking towards you from behind. You rapidly turn and see a figure aim a foreign object at you.")
    print("Without time to react the figure blasts you with a rifle, your death has come even quicker than expected.")
    print(name + " has died." + " GAME OVER")
    #Figure out how to close the game at this point
    #Add while alive loop
print("The river is now visible and you slowly approach the brink")
print("The river appears dirty, however your extreme thirst is to dangerous for you to go on without water.")
print("Type Yes if you choose to drink the water, or type No if you choose to go downstream in hopes of civilization and a clean water source?")
choice_2 = input()
if choice_2 == "No":
    print("You begin to head downstream in hopes of finding civilization.")
else:
    print("You cup your hands and rapidly consume as much water as possible")
    print("As you drink more and more water you quickly begin to realize that there is a strange mettalic taste in your mouth, but your thirst prevents you from stopping")
    print("Your heart starts to pound harder and harder and you feel a sharp pain rip through your stomach, you collapse quickly.")
    print("As you lie next to the river, pain flows through your entire body and your internal organs begin to shut down and your eyes start to close, you are dying")
    print("You should have never drank that water " + name + ", you are now dead")
    print("Game over")
    #Figure out how to close game at this point

print("You continue downstream and about a half mile into your journey a small house appears alongside the river")
print("You head towards the house")
print(" The house appears to be vacant, you open the door and creep through to find plenty of food, water and supplies")
print(" You drink the bottled water and eat the food that has been left for you.")
print(" You look around the house and notice a safe on the wall, however the safe has been locked with some type of mathematical key that can open it ")
print(" Type Yes to open the key and solve the cipher, type No to continue on your journey without opening the safe")
choice_3 = input()
if choice_3 == "Yes":
    print("You begin to look at the safe and realize that there is a riddle to unlock it")
else:
    print("You die")
answer_1 = int(input("A grandfather, two fathers, and two sons buy tickets for a show, how many tickets were purcahsed by them?: "))
if answer_1 == 3:
    print(" The safe begins to unlock")
elif print("That is not the correct answer"):
    print(" There is an equation that must be solved to finally unlock the safe ")
print("Enter three whole numbers that all add up to the answer of the previous riddle and the safe will unlock")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
if a + b + c == answer_1:
    print("The safe has unlocked")
else:
    print("The safe is not unlocked")
# This code below will be implemented into game to exhibit knowledge of numeric operator % soon
# num1 = (a//100)
#num2 = (a//10%10)
#num3 = (a%100%10)
#if num1 < num2 and num2 < num3:
  #print("YES")
#else:
  #print("NO")
               
               
#Need a mathematical cipher key that can be answered with python operators. 
