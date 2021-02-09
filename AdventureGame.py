# Adventure Game Assignment
# Loops and conditionals

'''
Ideas: Each dorm hall has a different number splattered across the walls
When put togther correctly, the numbers form a combo/password that unlocks the faculty offices
You meet King Struppa, and he challenges you to a duel on Wilson Field

Anytime you travel to a new location, there is a 40% chance that you run into a zombie and have to fight it
In order to survive, you have to enter a random set of strings in a time limit
This time limit may shorten as the game goes on, as well as the string of characters getting longer
Using KeyboardInterrupt, the user will not be able to see their input, making the challenge even more difficult

The user has 3 health points to start, and s/he will lose 1 hit point when failing an attack
Items around campus will give the user extra health
'''

import time
import random
import sys

''' TODO: Campus portion of game '''

# Declare variables
firstTimeEncounteringZombie = True
travelingRooms = False
crosswalkUnlocked = False
shiaHasCheese = True
isShiaAlive = True
isDeanPriceAlive = True
zombiesHavePatience = False
userHealthPoints = 3
unusedRandomNames = ["Ben", "Matt", "Sarah", "Jake", "Josh", "Jacob", "Ryan", "Ashley", "Ellie", "Ally", "Sam", "Emily", "Ayden", "Sydney", "Sean", "Lauren"]
usedRandomNames = []
charSet = "qwertyuiopasdfghjklzxcvbnm1234567890"
firstVisit1 = True
firstVisit2 = True
firstVisit3 = True
firstVisit4 = True
firstVisit5 = True
firstVisit6 = True
firstVisit7 = True
firstVisit8 = True
firstVisit9 = True
firstVisit10 = True
firstVisit11 = True
firstVisit12 = True
firstVisit13 = True
firstVisit14 = True
firstVisit15 = True
firstVisit16 = True
firstVisit17 = True

# Randomly assigns numbers to the dorm halls and declares their variables
morlanNumber = '{}'.format(random.randint(0,9))
pralleNumber = '{}'.format(random.randint(0,9))
henleyNumber = '{}'.format(random.randint(0,9))
glassNumber = '{}'.format(random.randint(0,9))
sandhuNumber = '{}'.format(random.randint(0,9))
'''Order of passcode is in the order variable assignment, so MPHGS'''
passcode = ''
passcode += morlanNumber
passcode += pralleNumber
passcode += henleyNumber
passcode += glassNumber
passcode += sandhuNumber

# Prints death texts and ends the game
def death():
    print("Holy baloney you lost all your health points!")
    print("You're dead man! Better luck next time :/ ")
    sys.exit(0)

# A simple function that tells the user to input something valid
def validOptionRequired():
    print("Input invalid. Please choose a valid option.")

# Contains all the lengthy discriptions of each area
def initialDescription(roomNum):

    # Pralle
    if roomNum == 1:
        print("You walk into the lobby of Pralle and notice numbers written on the wall on blood")
        print("It's just the number {} repeated over and over".format(pralleNumber))

    # Henley
    elif roomNum == 2:
        print("You walk into Henley, but the aura of cinematic talent isn't there like it usually is.")
        print("You look around and notice the walls have numbers on them, written in blood.")
        print("It's all the same number: {}".format(henleyNumber))

    # Glass
    elif roomNum == 3:
        print("You walk into glass. Your nose hurts, and you yell at the guys carrying a wall of glass across the street.")
        print("Why do they always do that?")
        print("You then walk into glass and hall and notice blood on the wall spelling out the number {} over and over again.".format(glassNumber))

    # Sandhu
    elif roomNum == 4:
        print("You walk into Sandhu and notice bl00d on the walls.")
        print("This time, the number {} is spelled out across the walls.".format(sandhuNumber))
        print("Why so much blood?")

    # Morlan
    elif roomNum == 5:
        print("You approach South Morlan and the place is trashed.")
        print("There's blood everywhere (spelling out the number {}); SoMo just looks like a wreck.".format(morlanNumber))
        print("You look over at NoMo and see the same level of messiness and blood; same old NoMo.")

    # User's dorm room
    elif roomNum == 6:
        print("You finally walk into your room after 4 failed attempts at the code on your door.")
        print("You feel at home, more relaxed than outside in the haze of the blood moon.")

    # Middle of dorm halls
    elif roomNum == 10:
        print("The streets are empty, and the air is quiet.")
        print("You look around and you see light coming from inside of one of dorm windows on the third floor of Henley.")
        print("The rest of the dorm windows in Sandhu and Henley are unlit.")

    # Piazza
    elif roomNum == 11:
        print("Welcome to the piazza!")
        print("A solid beam of light (or of power) shoots vertically out of the fountain and into the sky above.")
        print("There are lots of bulky wires going from the base of the fountain over to Wilson Field.")

    # Wilson Field
    elif roomNum == 16:
        pass

    # The corner of the intersection on the way to campus
    elif roomNum == 17:
        print("You walk to the corner and take a look at campus.")
        print("Absolutely empty, at least from what you can see from the intersection. One could say it's 'dead' quiet on campus.")
        print("Ba dum tischhhhhhhhhh")

# Calculates the chance of running into a zombie and enters encounterZombie if conditional is met
def randomZombieEncounter():

    # Prints traveling text
    traveling = "Traveling"
    for i in range(random.randint(2,5)):
        print (traveling)
        traveling += "."
        time.sleep(.7)

    # Chance is 40%
    num = random.randint(1, 10)
    if num < 5:
        encounterZombie()

# Runs combat with a normal zombie
def encounterZombie():

    # Declare variables
    global userHealthPoints
    global firstTimeEncounteringZombie
    global zombiesHavePatience

    # Prints combat instructions if this is first zombie encounter
    if firstTimeEncounteringZombie is True:
        print("You are about to enter combat.")
        print("Chapman zombies hate receptionists and their impressively high words per minute, so if one approaches, you must defend yourself with your typing skills.")
        print("If successful, the zombie will be tricked into thinking you answer phone calls for a living, and will leave you alone")
        print("(Zombies have a terrible memory though, so you'll have to reconvince him/her if you run into the same zombie a second time)")
        input("Press enter to continue")
        print("\nWhen a zombie approaches, you will be presented with a random string of characters that you must successfully type within a time limit")
        print("However, when you type, you won't be able to see your input, so be careful!")
        print("When you are done typing, you must press Enter and then Ctrl-c in order to submit your text")
        print("Only then will the zombie evaluate your typing skills")
        input("Press enter to begin combat")
        firstTimeEncounteringZombie = False

    print ("\nOh no! A zombie approaches!")
    zombieName = ""
    # Introduces zombie with random name
    if len(unusedRandomNames) != 0:
        nameSlot = random.randint(0, len(unusedRandomNames) - 1)
        zombieName = unusedRandomNames[nameSlot]
        print("And it's your old friend {}!!:((".format(zombieName))

    else:
        nameSlot = random.randint(0, len(usedRandomNames) - 1)
        zombieName = usedRandomNames[nameSlot]
        print("And it's your old friend {}!! S/he is back for seconds lmao".format(zombieName))

    # Prompts user to initiate combat
    print ("{} is approaching quickly!! Press enter to attack the zombie".format(zombieName))
    input()

    # Declare variables
    textToType = ''
    timeLimit = 5
    numOfChars = 5

    # Increases timeLimit if the user has prompted Dean Price to give the zombies patience, but also increases numOfChars
    if zombiesHavePatience is True:
        timeLimit += 2
        numOfChars += 1

    # Creates random set of chars called textToType
    for i in range(numOfChars):
        textToType += charSet[random.randint(0, len(charSet) - 1)]

    # Starts combat
    print('You have {} seconds to type: {}      Press enter and then ctrl-c when done'.format(timeLimit, textToType))

    # Runs timer and if timer completes, failure text prints and health point is taken away
    try:
        for i in range(0, timeLimit):
            time.sleep(1)
        userHealthPoints -= 1

        # DEATH
        if userHealthPoints == 0:
            death()

        print('Damn, you were too slow smh. {} got impatient and slapped you harder than any of your ex-girlfriends'.format(zombieName))
        print("You lost 1 health point, you have {} health point(s) remaining!".format(userHealthPoints))
        print("A zombie is going to attack you again (possibly a different one), and the text blocks are gonna repeat, are you ready?".format(zombieName))
        input()
        print("I'm not reading your response to that, you're getting attacked regardless of your preparedness")
        time.sleep(1)
        # Sends user back through combat
        encounterZombie()

    # Runs if ctrl-c is pressed, meaning the user is done with their input
    except KeyboardInterrupt:
        typedText = input()

        # Attack successful
        if typedText == textToType:
            print ("Congrats! Your typing skills impressed {} so much that s/he gave up and moved on with their day :D".format(zombieName))
            # Transfers unused name to used list
            usedRandomNames.append(unusedRandomNames[nameSlot])
            del unusedRandomNames[nameSlot]

        # Attack failed
        else:
            userHealthPoints -= 1

            # DEATH
            if userHealthPoints == 0:
                death()

            print("Damn, your fingers have failed you, your typing was crappy :( but hey at least you tried")
            print("{} just slapped you like s/he found out you made out with their significant other at last night's rager".format(zombieName))
            print("You lost 1 health point, you have {} health point(s) remaining!".format(userHealthPoints))
            print("A zombie is going to attack you again (possibly a different one), and the text blocks are gonna repeat, are you ready?")
            input()
            print("I'm not reading your response to that, you're getting attacked regardless of your preparedness")
            time.sleep(1)
            # Sends user back through combat
            encounterZombie()

# Runs combat with a boss
def bossFight(bossName):

    # Declare variables
    global userHealthPoints
    global firstTimeEncounteringZombie
    global isShiaAlive
    global isDeanPriceAlive

    # Declare variables
    timeLimit = 8
    numOfChars = 7
    bossHealth = 3

    if bossName == "Zombie Struppa":
        timeLimit = 9
        numOfChars = 8
        bossHealth = 5

    while bossHealth > 0:
        # Prompts user to initiate combat
        print ("{} is trying to attack you! Press enter to counter him with you typing skills!".format(bossName))
        input()

        textToType = ''
        # Creates random set of chars called textToType
        for i in range(numOfChars):
            textToType += charSet[random.randint(0, len(charSet) - 1)]

        # Starts combat
        print('You have {} seconds to type: {}      Press enter and then ctrl-c when done'.format(timeLimit, textToType))

        # Runs timer and if timer completes, failure text prints and health point is taken away
        try:
            for i in range(0, timeLimit):
                time.sleep(1)
            userHealthPoints -= 1

            # DEATH
            if userHealthPoints == 0:
                death()

            print('Damn, you were too slow smh. {} successfully shmacked the %#!& out of you'.format(bossName))
            print("You lost 1 health point, you have {} health point(s) remaining!".format(userHealthPoints))
            time.sleep(1)

        # Runs if ctrl-c is pressed, meaning the user is done with their input
        except KeyboardInterrupt:
            typedText = input()

            # Attack successful
            if typedText == textToType:
                print("Congrats! Your typing skills stunned {} just enough to allow you slap the bajeezus out of him".format(bossName))
                bossHealth -= 1
                print("{} lost 1 health point! He only has {} left!".format(bossName, bossHealth))
                time.sleep(1)

                # Increases toughness of combat
                numOfChars += 1

            # Attack failed
            else:
                userHealthPoints -= 1

                # DEATH
                if userHealthPoints == 0:
                    death()

                print("Damn, your fingers have failed you, your typing was crappy :( but hey at least you tried")
                print("{} just slapped you like he meant it".format(bossName))
                print("You lost 1 health point, you have {} health point(s) remaining!".format(userHealthPoints))
                time.sleep(1)

    # Runs after bossHealth reaches 0
    print("Congrats bruh! You defeated {}!".format(bossName))
    print("Nice work")

    # If boss is Shia
    if bossName == "Shia LaBeouf":
        # Declares him dead
        isShiaAlive = False

        # Checks to see if Shia has cheese
        if shiaHasCheese is True:
            print("You search Shia's body and find some cheese in his back pocket!")
            userHealthPoints += 1
            print("You have gained a health point! You now have {} health points!".format(userHealthPoints))

    elif bossName == "Dean Price":
        # Declares him dead
        isDeanPriceAlive = False

        # Declares global variable
        global zombiesHavePatience

        # Increases zombie patience
        print("The zombies in Chaptown take notice of your typing skills and have become more patient with you")
        print("From now on, when you fight a zombie, you have extra time to input your text!")
        print("However comma you will have to input more characters in order to satisfy the zombies.")
        zombiesHavePatience = True

    # End game - VICTORY
    elif bossName == "Zombie Struppa":
        print("Zombie Struppa begins to fall and crumble to his knees, screaming in agony as he realizes his defeat.")
        print("He fades into the air like Voldymort in Deathly Hallows Part 2 and the sky begins fade away from red.")
        print("The moon returns to its orginial color and the beam of light evaporates away from the fountain.")
        print("All the zombies come back to reality and oh, there goes gravity.")
        print("Everything becomes weightless and floatation becomes the new norm.")
        print("But hey, at least you saved Chaptown.")
        input("Press any key...")
        print("THE END")
        time.sleep(.5)
        sys.exit(0)

# Gathers input
userName = input("Welcome to the Chaptown game! Please enter your name:")
print("Nice to meet you, {}. What dorm hall do you reside in?".format(userName))
print("Just pick one if you don't live in one of the listed halls")
print("'1' for Pralle")
print("'2' for Henley")
print("'3' for Glass")
print("'4' for Sandhu")
print("'5' for Morlan")
homeDorm = int(input())

# Asks user if ready
userReady = input("Are you ready? 'yes' or 'no'")
while userReady != 'yes':
    if userReady == 'no':
        print("Okay...")
        time.sleep(.8)
        userReady = input("Are you ready now?")
    else:
        userReady = input("Please input a valid option")

print ("Alright let's begin.")
time.sleep(1)

# Introduction
print("===================================================================================================")
print("Interterm, week 3")
print("You awaken one morning feeling uneasy. Your roommate(s) are nowhere to be found, and it seems quieter outside than usual")
print("Your gut tells you to explore, so you make your way to the middle of the dorm halls - on the street in front of the caf")
print("On your way there, you notice that it's still dark out, but there's a slight red haze in the air.")
print("You look at the moon and its shines a dark red; the world looks like its coated in a crappy instagram filter.")

# Puts user in starting room
nextRoom = 10

'''MAIN LOOP'''
while nextRoom != 0:

    if nextRoom == 1: # Pralle
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit1 is True:
            print (initialDescription(nextRoom))
            firstVisit1 = False

        print("You stand in the Pralle lobby with the bloody {}s surrounding you".format(pralleNumber))
        print("1) Search for clues")
        print("2) Walk towards Henley")
        print("3) Head to the center of the residence halls")
        print("4) Head towards the intersection between here and Keck")
        if homeDorm == nextRoom:
            print("5) Head into your dorm room")
        response = int(input())

        if response == 1:
            print("You look around and find 0 clues, but you do realize something.. you're an idiot.")

        elif response == 2:
            nextRoom = 2
            travelingRooms = True

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        elif response == 4:
            nextRoom = 17
            travelingRooms = True

        elif response == 5:
            nextRoom = 6
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 2: # Henley
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit2 is True:
            print (initialDescription(nextRoom))
            firstVisit2 = False

        print("You stand in the Henley lobby. The menacing {}s on the wall feel like they're watching you.".format(henleyNumber))
        print("1) Go find the lit up room on the third floor")
        print("2) Head towards Pralle")
        print("3) Head towards the center of the residence halls")
        if homeDorm == nextRoom:
            print("4) Head into your dorm room")
        response = int(input())

        if response == 1 and isShiaAlive is True:
            print("You take the elevator cause the stairs are out of order and make your way to the third floor.")
            print("You walk down the hall and notice blood splattered across the walls and floor.")
            print("The blood becomes denser and darker as you get closer to the room")
            input("Press enter to knock on the door")
            print("Your attempt to knock failed because you instead decided to just walk in because the door the was very slightly ajar")
            print("As you walk in, you a hear a male voice say, 'Knock much?'")
            print("Your jaw drops as you instantly recognize his voice.")
            print("Actual, cannibal, Shia LaBeouf.")
            print("1) Attempt to slaughter him with your typing skills")
            print("2) Ask for some cheese")
            response2 = int(input())

            if response2 == 1:
                print("He prepares for action..")
                time.sleep(.8)
                bossFight("Shia LaBeouf")

            elif response2 == 2:
                # Check to see if Shia has any cheese
                if shiaHasCheese is True:
                    print("Shia scans you up and down for a few seconds and slowly licks his lips.")
                    print("But he shakes his head at himself, silently changing his mind.")
                    print("He reaches into his back pocket and pulls out a piece of cheese and hands it to you.")
                    input("Press enter to eat the cheese")
                    shiaHasCheese = False
                    print("You slowly eat the cheese, savoring every bite while simultaneously maintaing eye contact with Shia.")
                    print("He smiles and politely motions to the door.")
                    print("You leave feeling full and head back to the Henley lobby.")
                    print("You also gained 1 health point! You have {} total now.".format(userHealthPoints))
                    userHealthPoints += 1
                else:
                    print("He screams at you saying there's no cheese left and comes at with a knife")
                    print("Thankfully you are able to quickly run out of the room into the hall, exiting his jurisdiction.")
                    print("You head back to the Henley lobby.")

        elif response == 1 and isShiaAlive is False:
            print("As you slowly approach the third floor in the elevator, "\
            "you realize that on the off-chance that Shia is reincarnated into a superior form of himself,")
            print("he would surely defeat you in a second duel.")
            print("As the door opens, you stay in the elevator and ride it back down to the first floor, feeling like a coward.")

        elif response == 2:
            nextRoom = 1
            travelingRooms = True

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        elif response == 4:
            nextRoom == 6
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 3: # Glass
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit3 is True:
            initialDescription(nextRoom)
            firstVisit3 = False

        print("You stand in the middle of Glass, and you see the {}s surrounding you".format(glassNumber))
        print("1) Search for clues")
        print("2) Walk towards Morlan")
        print("3) Head to the center of the residence halls")
        if homeDorm == nextRoom:
            print("4) Head into your dorm room")
        response = int(input())

        if response == 1:
            print("You look around and find 0 clues, but you do realize something.. you're trash.")

        elif response == 2:
            nextRoom = 5
            travelingRooms = True

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        elif response == 4:
            nextRoom = 6
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 4: # Sandhu
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit4 is True:
            initialDescription(nextRoom)
            firstVisit4 = False

        print("You stand in the middle of Sandhu, the {}s surround you".format(sandhuNumber))
        print("1) Search for clues")
        print("2) Walk towards Henley")
        print("3) Head to the center of the residence halls")
        if homeDorm == nextRoom:
            print("4) Head into your dorm room")
        response = int(input())

        if response == 1:
            print("You look around and find 0 clues, but you do realize something.. you're a failure.")

        elif response == 2:
            nextRoom = 2
            travelingRooms = True

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        elif response == 4:
            nextRoom = 6
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 5: # Morlan
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit5 is True:
            initialDescription(nextRoom)
            firstVisit5 = False

        print("You stand in the center of the Morlan quad, surrounded by the {}s".format(morlanNumber))
        print("1) Head towards the Morlan kitchen for a snack")
        print("2) Head towards Glass")
        print("3) Head towards the center of the residence halls")
        if homeDorm == nextRoom:
            print("4) Head towards your dorm room")
        response = int(input())

        if response == 1 and isDeanPriceAlive is True:
            print("You enter the Morlan lounge and walk towards the kitchen.")
            input("Press enter to walk into the kitchen")
            print("As you enter the kitchen, you see Dean Price in an apron and a chef's hat with a hand towel over his shoulder.")
            print("He turns around to face you and you notice the spatula in his right hand.")
            print("As he sees your face, he says, 'Oh hey {}, what's goin on?'".format(userName))
            print("1) Prepare for battle")
            print("2) Say, 'nothing much wbu?'")
            response2 = int(input())

            if response2 == 1:
                print("Dean Price notices your battle stance and assumes the position.")
                print("Be ready to fight!")
                time.sleep(.8)
                bossFight("Dean Price")

            elif response2 == 2:
                print("Dean Price drops his spatula and says, 'About to battle some lame dood named {}...'".format(userName))
                print("Prepare for action!!")
                time.sleep(1)
                bossFight("Dean Price")

        elif response == 1 and isDeanPriceAlive is False:
            print("You walk into the kitchen where you once found Dean Price and this time find a buttload of snacks!")
            print("What snack do you want??")
            snack = input()
            print("You eat a {} and feel so replenished that you gain a health point!".format(snack))
            userHealthPoints += 1
            print("You now have {} health points!".format(userHealthPoints))

        elif response == 2:
            nextRoom = 3
            travelingRooms = True

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        elif response == 4:
            nextRoom = 6
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 6: # User's dorm room
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit6 is True:
            initialDescription(nextRoom)
            firstVisit6 = False

        print("You stand in the center of your room")
        print("1) Go to bed")
        print("2) Inspect the blood streaks on your wall")
        print("3) Head back to the street in front the caf, because any other location option just doesn't sound good right now")
        response = int(input())

        if response == 1:
            print("You close your eyes and try to sleep, but you suck at sleeping, so you get back up and cry about your poor sleeping skills")

        elif response == 2:
            print("You look at the wall and see the following letters smeared across the wall above your bed")
            print("\t MPHGS")
            time.sleep(1.5)
            print("What could it meeean?? Would could it represent?!?!?")

        elif response == 3:
            nextRoom = 10
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 10: # Middle of Residence Halls
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit10 is True:
            initialDescription(nextRoom)
            firstVisit10 = False

        print("You stand facing the caf.")
        print("1) Go inside the caf")
        print("2) Head inside Sandhu hall")
        print("3) Head towards Henley hall")
        print("4) Head towards Glass hall")
        print("5) Head towards Pralle hall")
        print("6) Head towards Morlan hall")
        print("7) Head towards the intersection leading to campus")
        response = int(input())

        if response == 1:
            print("You approach the caf doors and see that the door is boarded up with the soda machines")
            print("Looks like the caf workers have the right idea")

        elif response == 2:
            nextRoom = 4
            travelingRooms = True

        elif response == 3:
            nextRoom = 2
            travelingRooms = True

        elif response == 4:
            nextRoom = 3
            travelingRooms = True

        elif response == 5:
            nextRoom = 1
            travelingRooms = True

        elif response == 6:
            nextRoom = 5
            travelingRooms = True

        elif response == 7:
            nextRoom = 17
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 11: # Middle of Campus i.e. the Piazza
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit11 is True:
            initialDescription(nextRoom)
            firstVisit11 = False

        print("You stand in the center of campus, facing the fountain in the piazza.")
        print("1) Follow the wires to Wilson Field")
        print("2) Head back to the Residence Halls")
        repsonse = int(input())

        if response == 1:
            nextRoom = 16
            travelingRooms = True

        elif response == 2:
            nextRoom = 17
            travelingRooms = True

        else:
            validOptionRequired()

    elif nextRoom == 12: # Library
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit12 is True:
            initialDescription(nextRoom)
            firstVisit12 = False
    elif nextRoom == 13: # Faculty Offices
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit13 is True:
            initialDescription(nextRoom)
            firstVisit13 = False
    elif nextRoom == 14: # Dodge
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit14 is True:
            initialDescription(nextRoom)
            firstVisit14 = False
    elif nextRoom == 15: # Musco
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit15 is True:
            initialDescription(nextRoom)
            firstVisit15 = False
    elif nextRoom == 16: # Wilson Field
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit16 is True:
            initialDescription(nextRoom) # Nothing right now
            firstVisit16 = False

        print("You walk onto the grass and see a man sitting criss cross apple sauce in the center of the field.")
        print("The wires are going straight towards him; it seems as if he is sitting on them.")
        print("As you get closer, you recognize his face. That beautiful face. The president...")
        print("Struppa!")
        input("Press enter to interact with President Struppa")
        print("You say, 'what's good, G?' and he instantly begins to stand up, not saying a word")
        print("He takes the ends of the plugs and jams them into his back as if he had a port back there.")
        print("He begins to slowly grow into a super ultra mega presidential zombie; imagine Lupin in Prisoner of Azkaban, but bigger, and different..")
        input("Press enter to prepare for combat!")
        bossFight("Zombie Struppa")

    elif nextRoom == 17: # Intersection in between Pralle and Keck
        # Displays the lengthy initialDescription text if this is the frist time the area has been visited
        if firstVisit17 is True:
            initialDescription(nextRoom)
            firstVisit17 = False

        print("You stand at the corner adjacent to Pralle.")
        print("1) Try to cross the street to campus")
        print("2) Inspect the button that allows you to safely cross the street")
        print("3) Head into Pralle")
        print("4) Head into Henley")
        print("5) Head to the street in front of the caf")
        response = int(input())

        if response == 1:
            # Checks to see if the user is allowed to cross the street safely
            if crosswalkUnlocked is False:
                print("You can't cross the street without safely pressing the button!!    Idiot...")
            else:
                print("You successfully use the button to safely cross the street.")
                print("You head towards the center of campus.")
                # Sends you to the piazza
                nextRoom = 11
                travelingRooms = True

        elif response == 2:
            # This if else statement makes the keypad seem more mysterious if the user hasn't encountered a zombie yet
            if firstTimeEncounteringZombie is True:
                print("You look at the button and notice there's a keypad below it.")
            else:
                print("You look at the button and realize the zombies set up a keypad under the button")

            print("It seems like you have to enter a passcode in order to press the button..")
            print("1) Try entering the passcode")
            print("2) Stop inspecting a button")
            response2 = int(input())

            if response2 == 1:
                print("Please enter the passcode:")
                passcodeAttempt = int(input())

                if passcodeAttempt == int(passcode):
                    print("Ayyyyy, the passcode worked, nice job!")
                    crosswalkUnlocked = True
                else:
                    print("Damn, the passcode didn't work. Maybe try inputting correctly next time????")

            elif response2 == 2:
                print("You back away from the keypad")

            else:
                validOptionRequired()

        elif response == 3:
            nextRoom = 1
            travelingRooms = True

        elif response == 4:
            nextRoom = 2
            travelingRooms = True

        elif response == 5:
            nextRoom = 10
            travelingRooms = True

        else:
            validOptionRequired() # Intersection next to Keck and Pralle


    # Random Zombie Encounter Potential whenever the room changes
    if travelingRooms is True:
        travelingRooms = False
        randomZombieEncounter()
