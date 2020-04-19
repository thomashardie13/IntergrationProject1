# Intergration Project: Thomas Hardie: Text Based Adventure Game "Nerve"

#####################StartupCode#######################


print("Welcome to Nerve! This is a text based adventure game in which you will face many challenges, in order to beat the game, you shall navigate the challenges without death.")
print("If you die, you will be prompted with a notice to exit the program, even though it is still running, click yes and restart")
print("Please enter a name for your character")
name = input()
print("Well then, " + name + "!")
print("Please enter the age of your character")
age = int(input())
if age >= 18:
    print("Your character is old enough to play.")
else:
    print("Yikes youngling, lets see how long a child like you will last in Nerve")
#age = age * 2 // 2 + 40 - 20 - 20 exhibits knowledge of operators
print(age)
lives = int(input("What is the number that correlates to the present month?: "))
#Assigning lives based on month, random correlation just to exhibit knowledge of this code type:
if lives == 9 or lives == 4 or lives == 6 or lives == 11:
  print("You have 30 minutes for 30 days of that month")
elif lives == 1 or lives == 3 or lives == 5 or lives == 7 or lives == 12 or lives == 10 or lives == 8:
  print("You have 31 minutes for 31 days of that month")
elif lives == 2:
  print("You have 28 minutes for 28 days of that month")
print("I hope you are ready for what lies ahead, the control option will be stated when faced with a question")
print("choose which option is best fit for your travel in your belief and see how long you can last in Nerve. Good Luck")
print(" Nerve sequence beginning...")


####################BeginningNerveGame########################


print("You awake in a forest laying against a tall oak tree. You currently face dehydration, your mouth is dry, head is pounding and have no recollection of how you got there.")
print("There is a crashed truck near you, but unlike anything you have ever driven")
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
    exit()


#####################Second Choice Commence    #Figure out how to close the game at this point

    
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
    exit()
#####################Third Choice Commence    #Figure out how to close game at this point###########################

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
    print(" There is an riddle that must be solved to finally unlock the safe ")
    pritn("You lose")
    exit()
print("Enter three whole numbers that all add up to the answer of the previous riddle and the safe will unlock")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
if a + b + c == answer_1:
    print("The safe has unlocked")
else:
    print("The safe is not unlocked")
    exit()
#######################After Safe Unlocks#########################


print("The safe unlocks with nothing but a small key inside, you grab the key and begin out of the house, you are replenished")
print("You still do not know where you are or how you got there, and the use of the key causes you to ponder")
print("As you are walking out of the house a truck begins to approach, and you see armed men in the truckbed")
print("You can either make for the woods or hide in the house, both are equally risky as they will surely see you run to the woods")
print("Type House to hide in the house, or type Woods to run in the woods")
choice_5 = input()
if choice_5 ==  "House":
    print("You dart into the house and begin to look around for a hiding spot, you see the a cellar, however it is locked, you try using the key and it works")
    print("The cellar door creeks open, you swipe away cob webs and quietly shut it behind you, you begin down the creeky steps")
else:
    print("You start running for the woods, you hear the Men shout at you and bullets begin to reign, suddenly a bullet nips you in the leg and you tumble")
    print("One of the Men walk over to you and shoots you in the head")
    print("Game Over")
    exit()



#########################In the cellar##################


print("You feel your way around the pitch black cellar, and click on a light switch you felt")
print("The room becomes brighlty illuminated and you look around you in shock")
print("The room is full of dead bodies that appear to be exact clones of your own body")
print("How is this real you wonder, however when the cellar door opens you have no time to think, you jump in the pile of dead bodies and cover yourself with the dead")
print(" A man begins towards you placing another body down, you have an oppurtunity to attack him, type Attack to attack or type Hide to remain hiding")
choice_6 = input()
if choice_6 == "Attack":
    print("You shoot out of the pile of bodies and grab the Man by the neck choking him")
else:
    print("You choose to remain hiding and hope he does not see you")
    print("However, a rat crawls across your leg and begis chewing your flesh, you kick it off exposing your position to the Man who quickly drops the body and shoots you")
    print("You lose")
    exit()

############################# After Choice 6################
print(" You are able to kill the man and you grab his rifle, you make your way back up the cellar with new gained confidence as you are armed")
print(" You sprint towards the truck and start it with the keys in the ignition, however now the truck is being shot at by the other Men")
print(" You quickly reverse and floor it down the dirt road into apparent safety")
print(" Roughly five miles in, the dirt road approaches an electric gate, unlike anything you have seen, there is a small computer near the gate opening that might unlock it")
print(" You step out of the truck and head towards the computer, you have made it this far, you can't let this gate stop you from leaving this unknown land")
print("The computer prompts you with a series of mathematical questions, you must answer them correctly to unlock the gate")
########################## Math Questions #################

print(" The computer reads: What answer is a bigger number A. 15 * 3 or B. 7 * 6? ")
print(" Type A or B")
answer_q = input()
if answer_q == "A":
    print(" Correct")
else:
    print("Incorrect, you die")
    exit()
print("Next question: How many sides to an octagon")
print("Type the number of sides")
sides = input()
if sides == "8":
    print("Correct")
else:
    print("Incorrect, you die")
    exit()
print("One last question appears, an incomplete number pattern, finish the pattern to unlock the gate")
print(" 1,2,3,5,8,13,21, ")
print("Type the number that would come after 21 according the patterns logic, you have one attempt")
numb = input()
if numb == "34":
    print("Correct, gate opening")
else:
    print("You lose")
    exit()
print("The gate opens and you step into the car, finally, there must be freedom awaiting you!")
print("You drive through the gate and begin to relax thinking you made it out of the hell you were put in")
print("Surrounded by forest you slowly drive until a deer sprints accross the road and you strike it and then crash into a tree")
print("You step out of the car struggling to stand and tumble through the forest passing out next to a tree")
print("....Hours later...")
print("You awake in a forest laying against a tall oak tree. You currently face dehydration, your mouth is dry, head is pounding and have no recollection of how you got there.")
    
# This code below will be implemented into game to exhibit knowledge of numeric operator % soon
# num1 = (a//100)
#num2 = (a//10%10)
#num3 = (a%100%10)
#if num1 < num2 and num2 < num3:
  #print("YES")
#else:
  #print("NO")
               
               
#Need a mathematical cipher key that can be answered with python operators. 
