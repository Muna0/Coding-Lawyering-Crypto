

#Figuring out how users might respond
answer_A = ["A", "a"]   
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
    print ("After a party night out with friends, you wake up the "
    "next morning in a thick, gloomy forest. Your head is spinning and " 
    "you are feeling ill. As you stand and marvel at the unfamiliar "
    "forest setting, you hear a grotesque sound emitting behind you. A slobbering "
    " deformed creature is running towards you." 
    " You will:")
  
    print("""  A. Grab a nearby rock and throw it at the creature
    B. Lie down and wait to be eaten
    C. Run!!!!!""")
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print ("\nWelp, that was quick. "
        "\n\nYou die!")
    elif choice in answer_C:
        option_run()
    else:
        print (required)
        intro()

def option_rock(): 
    print ("\nThe creature is stunned, but regains control. It begins "
    "running towards you again. Will you:")

    print ("""  A. Run
    B. Throw another rock
    C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print ("\nYou decided to throw another rock, as if the first " 
        "rock thrown did much damage. The rock flew well over the "
        "creature's head. You missed. \n\nYou die!")
    elif choice in answer_C:
        option_cave()
    else:
        print (required)
        option_rock()

def option_cave():
    print ("\nYou were hesitant, since the cave was dark and "
    "ominous. Before you fully enter, you notice a shimmering sword on "
    "the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1 #adds a sword
    else:
        sword = 0
    print ("\nWhat do you do next?")

    print ("""  A. Hide in silence
    B. Fight
    C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nReally? You're going to hide in the dark? I think "
        "the creature can see very well in the dark, right? Not sure, but "
        "I'm going with YES, so...\n\nYou die!")
    elif choice in answer_B:
        if sword > 0:
            print ("\nYou laid in wait. The shimmering sword attracted "
            "the creature, which thought you were no match. As it walked "
            "closer and closer, your heart beat rapidly. As the creature "
            "reached out to grab the sword, you pierced the blade into "
            "its chest. \n\nYou survive!")
        else: #If the user didn't grab the sword
            print ("\nYou should have picked up that sword. You're "
            "defenseless. \n\nYou die!")
        if choice in answer_C:
            print ("As the creature enters the dark cave, you silently "
            "sneak out. You're several feet away, but the creature turns "
            "around and sees you running.")
            option_run()
        else:
            print (required)
            option_cave()

def option_run():
    print ("\nYou run as quickly as possible, but the creature's "
    "speed is too great. You will:")

    print ("""  A. Hide behind a boulder
    B. Trapped, so you fight!
    C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("You're easily spotted. "
            "\n\nYou die!")
    elif choice in answer_B:
        print ("\nYou're no match for the creature. "
        "n\nYou die!")
    elif choice in answer_C:
        option_town()
    else:
        print (required)
        option_run()
            
def option_town():
    print ("\nWhile frantically running, you notice a rusted "
    "sword lying in the mud. You quickly reach down and grab it, "
    "but miss. You try to calm your heavy breathing as you hide "
    "behind a dilapidated building, waiting for the creature to come "
    "charging around the corner. You notice a glowing flower "
    "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1 #adds a flower
    else:
        flower = 0
    print ("You hear the creature's heavy footsteps and ready yourself for "
        " impending doom")
  
    if flower > 0:
        print ("\nYou quickly hold out the glowing flower, "
        "hoping it will stop the creature. It does! The creature was looking "
        "for LOVE!!! AWWWWWWWWWW. "
        "\n\nThis got weird, but you survived!")
    else: #If the user didn't grab the sword
        print ("\nMaybe you should have picked up the flower. "
        "\n\nYou die!")

intro()