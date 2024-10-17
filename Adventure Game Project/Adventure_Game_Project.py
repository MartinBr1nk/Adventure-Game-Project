#----------Imports----------
import time
import random
import os
from Introduction import intro_sequence
import Player
import Enemies
import Weapons
import Wait
import ASCII
import Combat
from threading import Timer
import Score
from Terminal import terminal
import Goose


os.system('mode con: cols=180 lines=60')
#Resizes the window to fit ASCII art

#----------Variables----------
random_value = random.randint(0, 500)
#Random Value generated at the start of every run that can
#cause special events to happen
Player.name = "placeholder"
direction = "placeholder"
choice_loop = False
search_loop = False
skip = False
endless_mode = False
endless_enemies_killed = 0
endless_chaingun_cooldown = 0
successful_encounter = True
loss = 0
alt_fire = "h"
global circle

ruins_explored = False
village_explored = False


#----------Functions----------

def clear_screen():
    """
    'Clears' the screen by printing 75 new lines
    """
    for clear_x in range(75):
        print("\n")
        #"Clears" the screen by pushing everything else away

def print_slow(str):
    """
    Prints text letter-by-letter slowly
    """
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.1, 0.05))
    print("\n")
    #prints text letter-by-letter slowly


def print_fast(str):
    """
    Prints text letter-by-letter quickly
    """
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.0005, 0.0001))
    print("\n")
    #prints text letter-by-letter quickly


def print_very_fast(str):
    """
    Prints text letter-by-letter very quickly
    """
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.000005, 0.000001))
    print("\n")
    #prints text letter-by-letter REALLY quickly


def death_screen():
    """
    prints the death screen and exits the game
    """
    print_fast(ASCII.death_screen)
    exit()
    #Death screen

def menu():
    """
    Loads the menu
    """
    global skip
    global endless_mode
    global circle
    global through_menu
    menu_loop = True
    while menu_loop == True:
        print(ASCII.menu_title,
r"""
1 - START CAMPAIGN
2 - ENDLESS FIGHTING MODE
3 - HOW TO PLAY
4 - SETTINGS
5 - VIEW SCOREBOARD
6 - VIEW TERMINAL
7 - EXIT GAME""")

        menu_choice = str(input("WHERE DO YOU WANT TO NAVIGATE "
                                "TO?: ")).lower()
        if "1" in menu_choice or "start" in menu_choice \
            or "play" in menu_choice:

            print(r"""WHAT CIRCLE WILL YOU START IN?:
0 - THE MOUTH OF HELL
1 - LIMBO
""")
            menu_choice = str(input(":"))
            if "0" in menu_choice or "mouth" in menu_choice:
                menu_loop = False
                through_menu = False
                circle = 0
                Wait.wait(3)
                clear_screen()
                #Starts the game from the first area
            elif "1" in menu_choice or "limbo" in menu_choice:
                menu_loop = False
                through_menu = True
                circle = 1
                Wait.wait(3)
                clear_screen()
                #Starts the game from the second area
            else:
                print("INVALID OPTION")
                Wait.wait(1)

        elif "2" in menu_choice or "endless" in menu_choice:
            endless_mode = True
            menu_loop = False
            skip = True
            print("STARTING ENDLESS MODE")
            Wait.wait(1)
            clear_screen()
            #Starts endless mode

        elif "3" in menu_choice or "tutorial" in menu_choice or \
            "how" in menu_choice:
            clear_screen()
            f = open("text/Tutorial.txt", "r")
            print(f.read())
            f.close()
            input()
            clear_screen()
            #Prints tutorial from a text file.

        elif "4" in menu_choice or "settings" in menu_choice:
            print("""Settings:
1 - Skip waiting
2 - Wipe Scoreboard
""")
            setting_choice = input("Pick a setting to modify: ").lower()
            if "1" in setting_choice or "skip" in setting_choice:
                if Wait.time_skip == False:
                    Wait.time_skip = True
                elif Wait.time_skip == True:
                    Wait.time_skip = False
                Wait.wait(1)
                #Toggles between skipping Wait.wait or not skipping wait.wait
            elif "2" in setting_choice or "wipe" in setting_choice:
                setting_choice = input("Are you sure you want to wip the "
                                       "scoreboard? This CANNOT BE "
                                       "REVERSED. Type YES in UPPERCASE "
                                       "LETTERS if you are CERTAIN you want "
                                       "to wipe the scoreboard.: ")
                if "YES" in setting_choice:
                    Score.scoreboard_wipe()
                    #Wipes the scoreboard and creates a new scoreboard file
                    #withg nothing but the title in it.
                    print("SCOREBOARD WIPED!")
                else:
                    print("WIPE ABORTED.")
                Wait.wait(2)
                
            else:
                print("NO SETTING SELECTED.")
                Wait.wait(1)
                Wait.wait(3)
                clear_screen()
                #Opens the settings menu.
            clear_screen()

        elif "5" in menu_choice or "scoreboard" in menu_choice:
            clear_screen()
            f = open("text/Scoreboard.txt", "r")
            print(f.read())
            f.close()
            print("\n \n")
            input("Press enter when you are ready to return to the menu.")
            clear_screen()
            #Outputs the scoreboard from Scoreboard.txt in the text folder.

        elif "6" in menu_choice or "terminal" in menu_choice:
            clear_screen()
            terminal()
            clear_screen()
            #Opens the terminal.

        elif "7" in menu_choice or "exit" in menu_choice:
            print("CLOSING GAME...")
            exit()
            #Closes the game

        elif "9" in menu_choice or "skip" in menu_choice:
            print("skipping introduction!")
            skip = True
            Wait.wait(1)
            clear_screen()
            #skips the menu and intro sequence.

        else:
            print("ENTER A VALID OPTION.")
            Wait.wait(2)
            clear_screen()
            #If no valid option is entered, the menu continues to loop.


def overworld_quicktime(timeout, punish):
    """
    Quicktime dodging system
    """
    t = Timer(timeout, print, ["You got hit."])
    t.start()
    #starts the timer.
    start = time.time()
    #sets the start time.
    prompt = f"YOU HAVE {timeout} SECONDS TO DODGE. PRESS ENTER. \n"
    answer = input(prompt)
    t.cancel()
    #ends the timer.
    end = time.time()
    #sets the end time.
    time_taken = end - start
    #calculates the amount of time taken to react.
    if time_taken > timeout:
        print(f"DODGE FAILED, {punish} DAMAGE TAKEN.")
        Wait.wait(1)
        Player.current_health -= punish
        Player.DeathCheck()
        print(f"{Player.name} HAS {Player.current_health} FUEL REMAINING.")
        #if the player fails to react in time then they take damage.
    else:
        print("DODGED.")
        Wait.wait(1)
        #if the player reacts in time they dont take any damage.


#----------GAME----------

Goose.goose_check() #DO NOT REMOVE THE GOOSE CHECK.
menu()

game_loop = True
if endless_mode == False:
    while game_loop == True:
        if circle == 0:
            clear_screen()
            print_very_fast(ASCII.title)

            if skip == False:
                intro_sequence()
            else:
                Player.name = input("Name - ")
            print_slow(f"{Player.name} IS APPROACHING... THE MOUTH OF HELL")
            print_slow("IMPACT IMMINENT...")
            print("3...")
            Wait.wait(1)
            print("2...")
            Wait.wait(1)
            print("1...")
            Wait.wait(1)
            print_fast("IMPACT SUCCESSFUL")
            Wait.wait(1)
            for x in range(3):
                print("\n")

            input("As the dust clears, you can see a way forward through a "
                 "tunnel, obscured by smoke.")
            input("There are no other paths you can see. You decide to walk "
                 "through the obscured tunnel")
            input("You reach a dark, open room with three locked doors to "
            "your left, right and directly in front of you.")
            Wait.wait(1)

            Combat.standard_combat(Enemies.Filth.Name,
                                   Enemies.Filth.Health, 
                                   Enemies.Filth.Damage,
                                   Enemies.Filth.Range,
                                   Enemies.Filth.Healing)
            #Gets the Name, Heath, Damage, Range and player healing for combat
            Wait.wait(1)
            choice_loop = True
            while choice_loop == True:
                #Keeps the player in a loop until they make a valid choice
                direction = input("The doors have unlocked, allowing you to "
                                  "progress either left, right "
                                 "or forward. :").lower()
                if direction == "left":
                    choice_loop = False
                    print("\n")
                    input("The door to your left slams open and allows you "
                    "to pass through.")
                    input("Ahead of you lies a long, cylindrical metal "
                          "corridor.")
                    input("The walls have been heated to an extreme "
                          "temperature.")
                    input("Suddenly...")
                    print_slow("TRANSMISSION INCOMING...")
                    Wait.wait(1)

                    input("A voice comes from the speakers in your suits "
                          "cockpit:")
                    input(f"'Hello {Player.name}, this is a transmission "
                          "from Headquarters.'")
                    input("'It appears the Mouth of Hell has been overtaken "
                          "by an unknown force,'")
                    input("'We advise caution when attempting to -KZZZZZKT-'")
                    print_slow("TRANSMISSION OVER.")

                    Combat.standard_combat(Enemies.Stray.Name,
                        Enemies.Stray.Health,
                        Enemies.Stray.Damage, 
                        Enemies.Stray.Range,
                        Enemies.Stray.Healing)

            
                    choice_loop = True
                    input("The only way forward is to continue along the "
                          "corridor, it doesnt appear that there "
                          "are any more doors.")
                    input("However, you could attempt to look around this "
                          "room.")
                    input("This may be dangerous as the walls of the room "
                          "have been heated to an extreme temperature.")
                    while choice_loop == True:
                        #keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Inspect the Room? Yes/No: ").lower()
                        if "y" in choice:
                            input("You decide to inspect the room.")
                            print("!!! EXTREME HEAT DETECTED !!!")
                            Wait.wait(2)
                            print("!!! ENGAGING COOLING MECHANISM !!!")
                            Player.current_health = Player.current_health - \
                            100
                            Wait.wait(2)
                            print("YOU HAVE LOST 100 OUT OF "
                            f"{Player.max_health} FUEL.")
                            print(f"YOU HAVE {Player.current_health} FUEL "
                                  "LEFT")
                            Wait.wait(1)
                            input("You decide to continue along the "
                                  "corridor, as there does not appear to be "
                                  "anything else in this room")
                            choice_loop = False

                        elif "n" in choice:
                            input("You decide against inspecting the "
                                  "corridor.")
                            input("You continue along the corridor, as there "
                                  "does not appear to be anything else in "
                                  "this room")
                            choice_loop = False

                        else:
                            print("INVALID OPTION.")
                            Wait.wait(1)

                    input("Just as you left to the next room...")
                    Combat.standard_combat(Enemies.Schism.Name,
                                           Enemies.Schism.Health, 
                                           Enemies.Schism.Damage,
                                           Enemies.Schism.Range,
                                           Enemies.Schism.Healing)
                    input("Ahead of you lies a crossroad, Door A appears to "
                          "be the standard door with no differences to the "
                          "other doors you have been passing through.")
                    input("Door B has an 'EXIT' sign above it, it seems to "
                          "be damaged and would require a lot of force to "
                          "break through.")
                    input("If you want to get through door B you will have "
                          "to spend 25 - 100 fuel to smash through it.")
                    choice_loop = True
                    if choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Smash through the door?").lower()

                        if "y" in choice:
                            print_slow("PREPARING TO DESTROY DOOR")
                            loss = random.randint(25, 100)
                            Player.current_health = Player.current_health - \
                                loss
                            #The player loses 25 - 100 hp if they take this
                            #route

                            if Player.current_health <= 0:
                                print_slow("FUEL AT CRITICAL LEVELS")
                                print_slow("POWERING DOWN...")
                                death_screen()
                                #If the player runs out of fuel, they die.
                            else:
                                print_slow("ATTEMPT SUCCESSFUL")
                                print(f"{loss} FUEL LOST IN THE PROCESS. "
                                      f"YOU HAVE {Player.current_health} "
                                      "FUEL LEFT")
                                Wait.wait(1)
                                #outputs how much fuel the player lost and how
                                #much they have left
                            input("Behind the door is a large chasm in the "
                                  "ground, there appears to be a path to "
                                  "your left that may be connected to the "
                                  "path that Door A would take you to. You "
                                  "can see the shadow of a massive husk from "
                                  "this path.")
                            input("Suddenly...")
                            print_slow("PATH AHEAD DETECTED")
                            input("Your suit suddenly begins walking towards "
                                  "the chasm and prepares to jump in ")
                            input("The suit controls have been taken over by "
                                  "the suits AI, you cannot prevent its "
                                  "decent.")
                            print_slow("BEGINNING DECENT...")

                            circle = 1
                            choice_loop = False
                            #Gets the player out of the first area, 
                            #allowing them to prograss to the next area

                        elif "n" in choice:
                            input("You decide to take the standard door "
                                  "around")
                            input("Ahead of you lies a corridor filled with "
                                  "enemies, and at the end you can see a "
                                  "right turn that would lead you to where "
                                  "Door B is connected to.")

                            Combat.standard_combat(Enemies.Stray.Name,
                                                   Enemies.Stray.Health,
                                                   Enemies.Stray.Damage, 
                                                   Enemies.Stray.Range,
                                                   Enemies.Stray.Healing)

                            Combat.standard_combat(Enemies.Filth.Name,
                                                   Enemies.Filth.Health,
                                                   Enemies.Filth.Damage, 
                                                   Enemies.Filth.Range,
                                                   Enemies.Filth.Healing)

                            Combat.standard_combat(Enemies.Schism.Name,
                                                   Enemies.Schism.Health,
                                                   Enemies.Schism.Damage, 
                                                   Enemies.Schism.Range,
                                                   Enemies.Schism.Healing)

                            print_slow("LARGE ENEMY AHEAD, PREPARE YOURSELF")
                            Combat.standard_combat(Enemies.Colossus.Name, 
                                                   Enemies.Colossus.Health, 
                                                   Enemies.Colossus.Damage, 
                                                   Enemies.Colossus.Range, 
                                                   Enemies.Colossus.Healing)

                            input("Behind the turning is a large chasm in "
                                  "the ground, there appears to be a door "
                                  "to your right "
                            "that is connected to the path that Door B would "
                            "take you to.")
                            input("Suddenly...")
                            print_slow("PATH AHEAD DETECTED")
                            input("Your suit suddenly begins walking towards "
                                  "the chasm and prepares to jump in")
                            input("The suit controls have been taken over by "
                                  "the suits AI, you cannot prevent its "
                                  "decent.")
                            print_slow("BEGINNING DECENT...")

                            circle = 1
                            choice_loop = False
                            #Gets the player out of the first area, 
                            #allowing them to progress to the next area
                        else:
                            print("INVALID OPTION")
                            Wait.wait(1)

                elif direction == "right":
                    choice_loop = False
                    print("\n")
                    input("The door to your right slams closed behind you, "
                          "ahead of you lies a fork in the road with doors "
                          "to the left and right.")
                    input("Suddenly...")
                    print_slow("TRANSMISSION INCOMING...")
                    Wait.wait(1)

                    input("A voice comes from the speakers in "
                          "your suits cockpit:")
                    input(f"'Hello {Player.name}, this is a transmission "
                          "from Headquarters.'")
                    input("'It appears the Mouth of Hell has been overtaken "
                          "by an unknown force,'")
                    input("'We advise caution when attempting to -KZZZZZKT-'")
                    print_slow("TRANSMISSION OVER.")
                    Combat.standard_combat(Enemies.Filth.Name,
                                           Enemies.Filth.Health, 
                                           Enemies.Filth.Damage,
                                           Enemies.Filth.Range,
                                           Enemies.Filth.Healing)

                    choice_loop = True
                    input("There is a door to your left and a door to your "
                          "right")
                    while choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Do you go left or right?: ")
                        if "l" in choice:
                            choice_loop = False
                            input("You enter a long corridoor, with a large "
                                  "enemy blocking the path forward.")
                            input("You can see a potential exit ahead")
                            input("Suddenly...")
                            Combat.standard_combat(Enemies.Colossus.Name,
                                                   Enemies.Colossus.Health, 
                                                   Enemies.Colossus.Damage,
                                                   Enemies.Colossus.Range,
                                                   Enemies.Colossus.Healing)
                            input("You continue ahead through the corridoor "
                                  "and reach a chasm in the ground")
                            print_slow("PATH AHEAD DETECTED")
                            print_slow("BEGINNING DECENT...")

                            circle = 1
                            choice_loop = False
                            #Gets the player out of the first area, allowing
                            #them to progress to the next area

                        elif "r" in choice:
                            choice_loop = False
                            input("You enter a room resembling a cavern with "
                                  "no way through.")
                            input("You could explore the room to check "
                                  "if anything")
                            choice_loop = True
                            while choice_loop == True:
                                choice = input("Explore the room?: ").lower()
                                if "y" in choice:
                                    choice_loop = False
                                    input("You find a small lever hidden "
                                          "amongst the rocks in the room.")
                                    input("You decide to pull the lever.")
                                    input("The ground beneath you suddenly "
                                          "begins to open into a chasm")
                                    print_slow("PATH AHEAD DETECTED")
                                    print_slow("BEGINNING DECENT...")

                                    circle = 1
                                    choice_loop = False
                                    #Gets the player out of the first area, 
                                    #allowing them to progress to the next 
                                    #area
                                elif "n" in choice:
                                    choice_loop = False
                                    input("You notice a small tablet on "
                                          "the ground.")
                                    input("You pick it up and it reads:")
                                    print("Log #14")
                                    input(f"""The Mouth of Hell research 
station has been twisted into an industrial hellscape, we just woke up and the smell of smoke and fumes has flooded the entire station 
rooms have been twisted into a confusing labyrinth of industrial equipment and hellish creations that no sane person would make. 
We're all so scared and nobody is coming for us. Have we just been abandoned?""")
                                    #raw strings cant follow Pep-8 guidelines
                                    #without ruining how they look in-game.
                                    Wait.wait(1)
                                    input("Suddenly...")
                                    print_slow("Something wicked this way "
                                               "comes")
                                    Combat.standard_combat(
                                        Enemies.SomethingWicked.Name,
                                        Enemies.SomethingWicked.Health,
                                        Enemies.SomethingWicked.Damage,
                                        Enemies.SomethingWicked.Range,
                                        Enemies.SomethingWicked.Healing)
                                    #starts a easter egg fight that is
                                    #impossible to win
                                else:
                                    print("PLEASE CHOOSE A VALID OPTION.")
                        else:
                            print("PICK A VALID OPTION.")

                elif direction == "forward":
                    choice_loop = False
                    print("\n")
                    input("The door ahead of you slams open allowing you to "
                         "continue forward.")
                    input("The room behind the door is a large, winding "
                          "staircase above a massive spinning fan, "
                          "falling would result in instant death")
                    input("Suddenly...")
                    print_slow("TRANSMISSION INCOMING...")
                    Wait.wait(1)
                    input("A voice comes from the speakers in your suits "
                          "cockpit:")
                    input(f"'Hello {Player.name}, this is a transmission "
                          "from Headquarters.'")
                    input("'It appears the Mouth of Hell has been overtaken "
                          "by an unknown force,'")
                    input("'We advise caution when attempting to -KZZZZZKT-'")
                    print_slow("TRANSMISSION OVER.")

                    input("You can see many enemies lying on the staircase")
                    input("if you use a charge of your chaingun you may be "
                          "able to destroy the floor beneath some of the "
                          "enemies.")
                    choice_loop = True
                    while choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Do you use your chaingun?: ").lower()
                        if "y" in choice:
                            choice_loop = False
                            Weapons.chaingun_used = True
                            print("CHAINGUN USED, IT CANNOT BE USED AGAIN "
                                  "UNTIL REPAIRED")
                            #if the player uses the chaingun, they cant use
                            #it again
                            Wait.wait(1)
                            input("The staircase ahead crumbles infront of "
                                  "you, leaving a massive gap that you need "
                                  "to cross.")
                            input("However, all the enemies that you would "
                                  "have had to fought have fell and been "
                                  "shredded by the fan beneath.")
                            input("There is a huge gap between you and the "
                                  "next door.")
                            input("You'll have to jump the gap.")
                            input("To successfully jump the gap you will "
                                  "have to use HALF of your fuel to make the "
                                  "jump.")
                            input("You could risk it and lose 50 fuel to "
                                  "jump the gap but there is a chance you "
                                  "may fall and be shredded.")
                            choice_loop = True
                            while choice_loop == True:
                                #Keeps the player in a loop until they make a
                                #valid choice
                                choice = input("Play it safe and use half "
                                               "your fuel to jump the "
                                               "gap?: ").lower()
                                if "y" in choice:
                                    choice_loop = False
                                    Player.current_health = \
                                        Player.current_health / 2
                                    int(Player.current_health)
                                    #player loses half of their fuel if
                                    #they play it safe
                                    print(f"{Player.current_health} FUEL "
                                          "REMAINING.")
                                    #outputs how much fuel the player has left
                                    Wait.wait(1)

                                    input("You have successfuly jumped the "
                                          "gap.")
                                    input("The door at the end slams open "
                                          "and you can see a chasm that "
                                          "drops down for an indeterminate "
                                          "distance.")
                                    input("Suddenly...")
                                    print_slow("PATH AHEAD DETECTED")
                                    input("Your suit suddenly begins walking "
                                          "towards the chasm and prepares to "
                                          "jump in")
                                    input("The suit controls have been taken "
                                          "over by the suits AI, you cannot "
                                          "prevent its decent.")
                                    print_slow("BEGINNING DECENT...")

                                    circle = 1
                                    choice_loop = False
                                    #Gets the player out of the first area,
                                    #allowing them to progress to the next 
                                    #area

                                elif "n" in choice:
                                    choice_loop = False
                                    input("You brace yourself to jump.")
                                    jump_risk = random.randint(1, 2)
                                    if jump_risk == 1:
                                        print_slow("JUMP FAILED")
                                        Wait.wait(1)
                                        print_slow("EMERGENCY EJ-")
                                        death_screen()
                                        #if they fail the jump, they die
                                    else:
                                        Player.current_health = \
                                        Player.current_health - 50
                                        print(f"{Player.current_health} "
                                              "FUEL REMAINING.")
                                        Wait.wait(1)
                                        #if they successfully jump they only
                                        #lose 50 fuel

                                        input("You have successfuly jumped "
                                              "the gap.")
                                        input("The door at the end slams "
                                              "open and you can see a chasm "
                                              "that drops down for an "
                                              "indeterminate distance.")
                                        input("Suddenly...")
                                        print_slow("PATH AHEAD DETECTED")
                                        input("Your suit suddenly begins "
                                              "walking towards the chasm and "
                                              "prepares to jump in")
                                        input("The suit controls have been "
                                              "taken over by the suits AI, "
                                              "you cannot prevent its "
                                              "decent.")
                                        print_slow("BEGINNING DECENT...")

                                        circle = 1
                                        choice_loop = False
                                        #Gets the player out of the first 
                                        #area, allowing them to progress to 
                                        #the next area
                                else:
                                    print("INVALID OPTION.")
                                    Wait.wait(1)

                        elif "n" in choice:
                            choice_loop = False
                            input("You decide against using the chaingun.")
                            input("You'll have to fight through several "
                                  "tough enemies to get through now.")
                            for x in range(2):
                                Combat.standard_combat(Enemies.Stray.Name,
                                                       Enemies.Stray.Health,
                                                       Enemies.Stray.Damage,
                                                       Enemies.Stray.Range,
                                                       Enemies.Stray.Healing)
                            Combat.standard_combat(Enemies.Schism.Name,
                                                   Enemies.Schism.Health,
                                                   Enemies.Schism.Damage,
                                                   Enemies.Schism.Range,
                                                   Enemies.Schism.Healing)
                            print_slow("GIANT ENEMY AHEAD.")
                            Combat.standard_combat(Enemies.Colossus.Name, 
                                                   Enemies.Colossus.Health,
                                                   Enemies.Colossus.Damage,
                                                   Enemies.Colossus.Range,
                                                   Enemies.Colossus.Healing)
                            input("You can now continue further.")
                            #Enemy gauntlet

                            input("The door at the end slams open and you "
                                  "can see a chasm that drops down for a "
                                  "indeterminate distance.")
                            input("Suddenly...")
                            print_slow("PATH AHEAD DETECTED")
                            input("Your suit suddenly begins walking towards "
                                  "the chasm and prepares to jump in")
                            input("The suit controls have been taken over by "
                                  "the suits AI, you cannot prevent its "
                                  "decent.")
                            print_slow("BEGINNING DECENT...")

                            circle = 1
                            choice_loop = False
                            #Gets the player out of the first area,
                            #allowing them to progress to the next area

                        else:
                            print("INVALID OPTION.")
                            print("\n")
                            Wait.wait(1)

                else:
                    print("PICK A VALID DIRECTION.")
                    print("\n")
                    Wait.wait(1)
    
                
                
        elif circle == 1:
            Wait.wait(3)
            clear_screen()
            print_very_fast(ASCII.title)

            if through_menu == True:
                #if the player got to limbo through the menu,
                #they are forced to go through the intro or choose a name.
                if skip == False:
                    intro_sequence()
                else:
                    Player.name = input("Name - ")
            print_slow(f"{Player.name} IS APPROACHING... CIRCLE 1 - LIMBO")
            print_slow("IMPACT IMMINENT...")
            print("3...")
            Wait.wait(1)
            print("2...")
            Wait.wait(1)
            print("1...")
            Wait.wait(1)
            print_fast("IMPACT SUCCESSFUL")
            Wait.wait(1)
            for x in range(3):
                print("\n")

            input("Ahead of you lies a vast, endless field "
            "filled with small villages and castles.")
            input("The arcitechture of this circle of hell appears "
            "to be inspired by the medieval period")
            input("However, the trees and grass appear to be fake")
            input("the leaves appear to be flickering in an out of existence,"
            " as if they were just holograms")
            input("The sky appears to look like a CRT screen despite the "
                  "fact that it appears to stretch on forever")
            input("Calming music and sounds of birds play from small poorly "
                  "hidden speakers throughout the field")
            input("Ahead of you lies a fork in the road.")
            input("To the left there is a large castle you could attempt "
                  "to enter.")
            input("To the right there is a small village.")


            choice_loop = True
            while choice_loop:
                #Keeps the player in a loop until they make a valid choice
                choice = input("Do you go left or right?: ").lower()
                if "l" in choice:
                    choice_loop = False
                    input("You walk along the path to the castle.")
                    input("As you walk, you notice marks of war along the "
                          "landscape.")
                    input("They appear to be marks from a battle using "
                          "similar weaponry that was used in the war.")
                    Combat.standard_combat(Enemies.Crawler.Name,
                                           Enemies.Crawler.Health,
                                           Enemies.Crawler.Damage,
                                           Enemies.Crawler.Range,
                                           Enemies.Crawler.Healing)


                    input("You approach the castle gates.")
                    input("Suddenly...")
                    print_slow("THREAT DETECTED")
                    print("CRAWLER APPRO-")
                    Wait.wait(1)
                    #fake-out combat encounter
                    input("A mangled, deformed suit slams onto the ground "
                          "from inside the castle "
                          "and destroys all the enemies around you")
                    input("It then leaps away and seems to be heading "
                          "towards the castle.")
                    input("An unidentified broadcast is being forced "
                    "to transmit over your comms.")
                    print_slow("THE ONLY WAY FORWARD IS THROUGH THE CASTLE.")
                    print_slow("I'LL SEE YOU INSIDE.")
                    print_slow("SYSTEM MESSAGE: ENEMY IS FAR BEYOND YOUR "
                    "COMBAT CAPIBILITIES.")
                    input("You'll have to upgrade your equipment.")
                    input("You can try to explore limbo to try and find "
                          "an upgrade.")

                elif "r" in choice:
                    choice_loop = False
                    input("You approach the small village.")
                    input("It appears to be completely devoid of life.")
                    input("Suddenly...")
                    Combat.standard_combat(Enemies.Colossus.Name,
                                           Enemies.Colossus.Health,
                                           Enemies.Colossus.Damage,
                                           Enemies.Colossus.Range,
                                           Enemies.Colossus.Healing)

                    input("There is a shattered suit in the center of the "
                          "village.")
                    input("You could use the scrap from it to repair your "
                          "chaingun")
                    Wait.wait(1)
                    if Weapons.chaingun_used == True:
                        choice_loop = True
                        while choice_loop == True:
                            choice = input("Do you want to use the scrap to "
                                           "repair your chaingun?").lower()
                            if "y" in choice:
                                Weapons.chaingun_used = False
                                choice_loop = False
                                print_slow("CHAINGUN RESTORED")
                                input("You can hear shuffling around you...")
                                input("Suddenly...")
                                #Repairs the players chaingun, letting them
                                #use it again.
                                Combat.standard_combat(Enemies.Crawler.Name,
                                                       Enemies.Crawler.Health,
                                                       Enemies.Crawler.Damage,
                                                       Enemies.Crawler.Range,
                                                      Enemies.Crawler.Healing)
                                input("The destroyed suit appears to have "
                                      "been destroyed by similar weaponry "
                                      "to what the suits come with")
                                input("It's filled with bullet holes.")
                            elif "n" in choice:
                                input("You decide against using the scrap to "
                                      "repair your chaingun")
                                choice_loop = False
                            else:
                                print("INVALID CHOICE.")
                                Wait.wait(2)

                    else:
                        input("However, your chaingun does not need to be "
                              "repaired.")

                    input("You continue on through the village.")
                    input("You can hear several creatures scurrying "
                          "around you")
                    input("Do you want to engage in combat or run?: ")
                    input("Before you can make a decision several demons "
                          "surround you on all sides.")
                    print_slow("THREAT DETECTED")
                    print("CRAWLER APPRO-")
                    Wait.wait(1)
                    #fake-out combat encounter
                    input("A mangled, deformed suit slams onto the ground "
                          "and destroys all the enemies around you")
                    input("It then leaps away and seems to be heading "
                          "towards the castle.")
                    input("An unidentified broadcast is being forced "
                    "to transmit over your comms.")
                    print_slow("THE ONLY WAY FORWARD IS THROUGH THE CASTLE.")
                    print_slow("I'LL SEE YOU THERE.")
                    print_slow("SYSTEM MESSAGE: ENEMY IS FAR BEYOND YOUR "
                    "COMBAT CAPIBILITIES.")
                    input("You'll have to upgrade your equipment.")
                    input("You can try to go towards the castle "
                          "or explore limbo in hopes of finding an upgrade")
                    choice_loop = True
                    while choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Explore or attempt to go the "
                        "castle: ").lower()
                        if "castle" in choice:
                            print("ERROR, NOT STRONG ENOUGH TO ATTEMPT ENTRY")
                            Wait.wait(2)
                        elif "explore" in choice:
                            choice_loop = False
                            input("You decide to explore limbo in hopes "
                                  "of finding an upgrade.")
                        else:
                            print("INVALID OPTION")
                            Wait.wait(2)
                else:
                    print("INVALID OPTION")
                    Wait.wait(2)

            print("\n")
            input("You begin to look around limbo for an upgrade")
            input("You make it up to a vantage point where you can see "
                      "the landscape around you.")
            
                #no matter what you do, you are always railroaded to
                #explore limbo.
            search_loop = True
            while search_loop == True:
                #Keeps the player in a loop until they finish the exploration
                #section
                print("You can see Ruins, a burning village and a church")
                choice = input("Where do you go?: ").lower()
                if "ruins" in choice and ruins_explored == False:
                    input("You approach the ruins.")
                    input("They are just solid stone.")
                    input("No engravings or signs of wear")
                    input("They appear to be more like props rather than "
                    "actual ruins, lacking any wear or signs of use.")
                    input("There doesnt appear to be anything of "
                          "use here.")
                    input("Before you can leave a part of the ruins begins "
                    "to move...")
                    Combat.standard_combat(Enemies.Guardian.Name,
                                           Enemies.Guardian.Health,
                                           Enemies.Guardian.Damage,
                                           Enemies.Guardian.Range,
                                           Enemies.Guardian.Healing)
                    ruins_explored = True
                    #The ruins have been explored, so the player cannot return
                    #as there is nothing they need here.
                    input("On a pillar in the ruins, a glowing 'I' forms")
                    input("You go back to the vantage point.")
                    print("\n")
                    #Forces the player to explore this area
                elif "village" in choice and village_explored == False:
                    input("You approach the burning village.")
                    input("As you approach the fire, you can notice that "
                          "it seems fake, it flickers between different "
                          "frames as if it is animated.")
                    input("The houses seem untouched by the blaze that "
                          "englufs them.")
                    input("It doesnt seem like you're meant to be here")
                    input("The floor and walls around you begin to form "
                    "something...")
                    Combat.standard_combat(Enemies.Shade.Name,
                                           Enemies.Shade.Health,
                                           Enemies.Shade.Damage,
                                           Enemies.Shade.Range,
                                           Enemies.Shade.Healing)
                    village_explored = True
                    input("In a tower in the center of the village, a "
                    "glowing 'II' forms, the fire also suddenly stops in a "
                    "flash of light.")
                    input("You go back to the vantage point.")
                    print("\n")
                    #Forces the player to explore this area

                elif "church" in choice:
                    input("The church doors are sealed shut by two metal "
                          "bars.")
                    input("To the side of each bar, there is an engraving")
                    input("The top bar has 'I' engraved next to it and the "
                          "bottom bar has 'II' engraved next to it.")
                    if ruins_explored == True and village_explored == False:
                        input("The 'I' engraving is glowing, but the door "
                              "is still sealed")
                        input("You return to the vantage point as there is "
                              "nothing you can do here at the moment.")
                        print("\n")
                    elif ruins_explored == False and village_explored == True:
                        input("The 'II' engraving is glowing but the door "
                              "is still sealed")
                        input("You return to the vantage point as there is "
                              "nothing you can do here at the moment.")
                        print("\n")
                    elif ruins_explored != True and village_explored != True:
                        input("You return to the vantage point as there is "
                              "nothing you can do here at the moment.")
                        print("\n")
                    #Various outcomes for if you have not explored enough
                    elif ruins_explored == True and village_explored == True:
                        input("Both engravings begin to glow and the door "
                              "slams open.")
                        input("The inside of the church is dimly lit, "
                              "a large stained window portraying an angel "
                              "overlooks the interior")
                        input("Rows of pews fill the building.")
                        input("You can see a lone skeleton sitting to the "
                              "left, in the front pews.")
                        input("It is praying.")
                        Wait.wait(3)
                        input("A small box sits below the stained window.")
                        print_slow("UPGRADE DETECTED.")
                        input("You walk towards the box.")
                        input("You open the box, inside is a small computer "
                              "chip, held together by a red substance.")
                        input("It appears to be pulsating.")
                        print_slow("INSTALLING UPGRADE...")
                        print_fast("""UPGRADE UNLOCKED!
You can now channel hell energy during boss fights.
This will give a massive strength boost and will let
you stand a chance against tough enemies.""")
                        Wait.wait(3)
                        input("You can now go towards the castle.")
                        input("You leave the church and close the door "
                              "behind you, leaving the skeleton in peace.")
                        search_loop = False
                        #Allows the player to leave the exploration section
                        for x in range(3):
                            print("\n")
                
                else:
                    print("INVALID OPTION / AREA ALREADY EXPLORED")
                    print("\n")
                    Wait.wait(2)

            input("You begin to make your way back to the castle.")
            input("The sky flickers and shuts off.")
            input("It then flickers back to life, but instead of being day, "
                  "the sky is now dark and starry, a fake moon overlooks "
                  "the landscape.")
            Wait.wait(2)

            input("You managed to return back to the castle.")
            input("The gates of the castle slam open...")

            input("The castle has stained glass windows lining a majority of "
                  "the walls, despite the fact that they wouldnt lead outside"
                  "light still floods through them.")
            input("Red carpet lines the floor.")
            input("You need to enter the central chamber of the castle to "
                  "continue to the next circle.")
            input("Ahead of you lies three paths, the left and right path "
                  "go to places you cannot see while the forward path goes "
                  "directly to the central chamber.")
            input("However, the forward path seems to be crumbling into the "
                  "ground, the extra weight of you walking through this path "
                  "might cause the ground to fall beneath you.")
            input("The forward path crumbling is VERY LIKELY if you "
                  "take it.")

            choice_loop = True
            while choice_loop == True:
                #Keeps the player in a loop until they make a valid choice
                choice = input("What path do you take?: ")
                if "left" in choice:
                    choice_loop = False
                    print("\n")
                    input("You go left.")
                    input("The corridor ahead warps and transforms in front "
                          "of you.")
                    input("It appears to stretch on forever")
                    input("However, you can see a mirror of yourself also "
                          "appearing over and over.")
                    input("It seems like this corridor is just mirroring "
                          "itself.")
                    input("Looking behind you, you can see that the corridor "
                          "is mirroring behind you as well.")
                    input("You can either try to walk through the corridor "
                          "or attempt to shoot down the corridor and see if "
                          "you can escape")

                    choice_loop = True
                    while choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        choice = input("Do you walk through the corridor or "
                        "shoot down the corridor? ")
                        if "walk" in choice:
                            choice_loop = False
                            input("You begin walking through the corridor.")
                            input("After a certain point you notice your "
                                  "vision flicker for a moment and you warp "
                                  "back a few steps.")
                            input("There doesnt seem to be any way out.")
                            input("The only thing you could do is shoot the "
                                  "stained glass windows on the side of the "
                                  "corridor.")
                            input("You shoot a window.")
                            Wait.wait(1)
                            input("The mirror image around you shakes and "
                                  "distorts a little.")
                            input("Hell mass pours out of the window!")
                            for x in range(3):
                                Combat.standard_combat(Enemies.Shade.Name,
                                                       Enemies.Shade.Health,
                                                       Enemies.Shade.Damage,
                                                       Enemies.Shade.Range,
                                                       Enemies.Shade.Healing)

                    
                        elif "shoot" in choice:
                            while True:
                                #Keeps the player in a loop until they make a
                                #valid choice
                                choice = input("Do you shoot at a wall "
                                               "ahead of you or directly at "
                                               "yourself? ")
                                if "wall" in choice:
                                    input("The bullet mirrored itself, "
                                          "appearing behind you.")
                                    input("Nothing appeared to change.")
                                    break
                                elif "self" in choice:
                                    input("You shoot at yourself.")
                                    death_screen()
                                    #what would obviously happen if you shot
                                    #yourself in an endlessly repeating
                                    #corridor
                                else:
                                    print("INVALID OPTION")
                                    Wait.wait(2)
                        else:
                            print("INVALID OPTION")
                            Wait.wait(2)

                    input("The mirror image around you shatters and "
                          "you can continue down the corridor.")
                    input("You reach the end of the corridor and you can"
                          "see a path towards the inner chamber.")
                    input("Suddenly a swarm of enemies smash through the "
                          "windows!")
                    Combat.standard_combat(Enemies.Schism.Name,
                                           Enemies.Schism.Health,
                                           Enemies.Schism.Damage,
                                           Enemies.Schism.Range,
                                           Enemies.Schism.Healing)
                    Combat.standard_combat(Enemies.Guardian.Name,
                                           Enemies.Guardian.Health,
                                           Enemies.Guardian.Damage,
                                           Enemies.Guardian.Range,
                                           Enemies.Guardian.Healing)
                    for x in range (3):
                        Combat.standard_combat(Enemies.Crawler.Name,
                                               Enemies.Crawler.Health,
                                               Enemies.Crawler.Damage,
                                               Enemies.Crawler.Range,
                                               Enemies.Crawler.Healing)
                    Combat.standard_combat(Enemies.Colossus.Name,
                                           Enemies.Colossus.Health,
                                           Enemies.Colossus.Damage,
                                           Enemies.Colossus.Range,
                                           Enemies.Colossus.Healing)
                    #Enemy rush before reaching the inner chamber

                elif "right" in choice:
                    choice_loop = False
                    print("\n")
                    for x in range (3):
                        Combat.standard_combat(Enemies.Crawler.Name,
                                               Enemies.Crawler.Health,
                                               Enemies.Crawler.Damage,
                                               Enemies.Crawler.Range,
                                               Enemies.Crawler.Healing)
                    input("You walk down the right corridor.")
                    input("You enter a grand dining hall filled with food, "
                          "tables, chairs and candles.")
                    input("Upon closer inspection, the food seems to have "
                          "the same texture as the flesh that demons have.")
                    input("The furniture also seems to have this fleshy "
                          "texture.")
                    input("Suddenly some of the furniture begins to move!")
                    Combat.standard_combat("Chair " + Enemies.Mimic.Name,
                                           20,
                                           50,
                                           1,
                                           25)
                    Combat.standard_combat("Table " + Enemies.Mimic.Name,
                                           50,
                                           50,
                                           1,
                                           50)
                    Combat.standard_combat("Food " + Enemies.Mimic.Name,
                                           5,
                                           5,
                                           1,
                                           10)
                    #Mimics have custom stats, as it depends on what object
                    #they are mimicing.
                    input("The other peices of furniture around you begin to "
                          "shake and emit a horrific screech.")
                    input("They begin to clump together.")
                    input("Bricks, Chairs, Tables and bits of food form a "
                          "colossal demon...")
                    Combat.standard_combat("Greater Castle " +
                                           Enemies.Mimic.Name,
                                           300,
                                           50,
                                           1,
                                           500)
                    input("The demon shatters back into its individual "
                          "peices")
                    input("Bits of wood and food cover the previously "
                          "organised dining room.")
                    choice_loop = True
                    while choice_loop == True:
                        #Keeps the player in a loop until they make a valid
                        #choice
                        input("The dining room has two doors on either side "
                              "that could lead you further in.")
                        input("The door to your left follows the design of "
                              "everything else in the castle so far while "
                              "the door on the right is visibly damaged and "
                              "no light is coming in from underneath it.")
                        choice = input("What door do you go "
                                       "through?: ").lower()
                        if "left" in choice:
                            choice_loop = False
                            print("\n")
                            input("You walk through the left door.")
                            input("Everything here is completely normal and "
                                  "nothing is out of the ordinary.")
                            input("This path seems to be incredibly boring.")
                            input("You cant help but think about how much "
                                  "more intresting the other path would "
                                  "have been.")
                            Wait.wait(3)
                            input("You can see the path to the inner "
                                  "chamber.")
                            input("Theres a tiny mimic on the ground.")
                            input("It looks like its mimicing a brick.")
                            input("You step on it.")
                            Player.current_health += 10
                            Player.HealthCheck()
                            print_slow(f"10 FUEL RESTORED.")
                            print_slow(f"{Player.name} HAS "
                                       f"{Player.current_health} "
                                  "FUEL REMAINING.")
                            #output how much health the player restores.
                            input("You look behind you.")
                            input("The door back is gone.")
                            input("You couldnt go back if you wanted to.")
                            input("You can feel the ground beneath you "
                                  "rumbling.")
                            input("That other path would have been very "
                                  "intresting.")
                            input("Now you'll never know what is behind that "
                                  "door.")
                            Wait.wait(3)

                        elif "right" in choice:
                            choice_loop = False
                            print("\n")
                            input("You open the door.")
                            input("It's pitch black and stairs decend for an "
                                  "indeterminate distance")
                            input("Something kicks you down the stairs!")
                            Player.current_health = Player.current_health - \
                                                                        100
                            print_slow("LOST 100 FUEL")
                            Player.DeathCheck()
                            print_slow(f"{Player.current_health} FUEL "
                                       "REMAINING.")
                            print("\n")
                            input("You cant see anything.")
                            print_slow("LIGHT ACTIVATING...")
                            input("You suits light activates")
                            input("This room appears to be a cellar, its "
                                  "filled with barrels of food and drink.")
                            input("You walk further through the cellar.")
                            input("There seems to be a path through the "
                                  "cellar into the innter chamber.")
                            input("The cellar begins to shake...")
                            input("A colossal demon emerges from the ground "
                                  "beneath you")
                            print_slow("ENHANCED FIGHTING CAPTIBILITIES NEED "
                                       "TO BE SAVED FOR THE FINAL ENCOUNTER.")
                            print_slow("RUN AS FAST AS YOU CAN.")

                            #Quicktime event
                            print("QUICKTIME START.")
                            Wait.wait(1)
                            print("You begin to run.")
                            Wait.wait(1)
                            print("A barrel comes flying towards you!")
                            overworld_quicktime(5, 50)
                            print("KEEP RUNNING!!!")
                            Wait.wait(1)
                            print("Shelves come crashing down!")
                            Wait.wait(1)
                            overworld_quicktime(2, 50)
                            print("Nearly there!!!")
                            Wait.wait(1)
                            print("The cellar begins to crumble around "
                                  "you...")
                            Wait.wait(1)
                            print("The ceiling beings to fall!!")
                            Wait.wait(1)
                            print("You need to slide")
                            overworld_quicktime(3, 150)
                            print("You can see the light leading to the "
                                  "exit!")
                            Wait.wait(1)
                            print("QUICKTIME OVER.")
                            Wait.wait(1)
                            #Quicktime even end

                            input("You make it out of the cellar.")
                            input("The demon that was chasing you has been "
                                  "crushed by the falling cellar.")

                        else:
                            print("INVALID OPTION")
                            Wait.wait(2)

                elif "forward" in choice:
                    choice_loop = False
                    print("\n")
                    input("You walk into the path directly ahead of you.")
                    if random_value == 486:
                        input("By sheer luck, the path manages to hold "
                              "up and you make it across.")
                        input("It crumbles behind you...")
                        #if you get the number 486 from the random
                        #number generator at the start of the game
                        #you get VERY lucky and get to skip the entire
                        #castle segment. 
                    else:
                        print_slow("WARNING - PATH UNSTABLE")
                        input("The path begins to fall underneath you.")
                        input("You begin to fall further")
                        for x in range(5):
                            print("and further...")
                            Wait.wait(1)
                        death_screen()
                        #You will ususally just die though.
                else:
                    print("INVALID OPTION")
                    Wait.wait(2)
                    input("Ahead of you lies three paths, the left and "
                          "right path go to places you cannot see while the "
                          "forward path goes directly to the central "
                          "chamber.")
                    input("However, the forward path seems to be crumbling "
                          "into the ground, the extra weight of you walking "
                          "through this path might cause the ground to fall "
                          "beneath you.")
                    input("The forward path crumbling is VERY LIKELY if you "
                          "take it.")

            input("You finally make it to the inner chamber...")
            input("There is a stained glass window overlooking the chamber.")
            input("The light that was beaming down becomes blocked by a "
                  "shadow")
            input("Suddenly...")
            input("The window shatters.")
            input("You stand face to face with the enemy.")
            input("Your cameras flicker on for a brief second!")
            #Boss fight start!
            ASCII.hijacked_intro_animation()
            Wait.wait(3)
            clear_screen()
            while Combat.win_condition != True:
                Combat.hijacked_boss_fight(Enemies.Hijacked_1.Name, 
                               Enemies.Hijacked_1.Health)
                if Combat.loose_condition == True:
                    print_fast(ASCII.death_screen)
                    Wait.wait(1)
                    print("\n")
                    input("You fall down, defeated but something is off...")
                    input("The room around you warps and changes.")
                    input("You have been placed just outside the inner "
                          "chamber, with no injuries.")
                    print_slow("AGAIN.")
                    Player.b_current_health = 2000
                    Wait.wait(1)

            input("The enemy falls to the ground, damaged and defeated.")
            input("It scrambles to escape back through the window it came "
                  "from")
            print_slow("I'LL BE BACK.")
            input("The moon above shines into the chamber.")
            input("Suddenly...")
            input("A chasm beigins to opem up in the center of the chamber!")

            print_slow("PATH AHEAD DETECTED")
            input("Your suit suddenly begins "
                  "walking towards the chasm and "
                  "prepares to jump in")
            input("The suit controls have been "
                  "taken over by the suits AI, "
                  "you cannot prevent its "
                  "decent.")
            print_slow("BEGINNING DECENT...")
            circle += 1
            choice_loop = False
            Wait.wait(1)
            #Lets the player go to the next circle

        elif circle == 2:
            game_loop = False
            clear_screen()
            print("Circle 2 - Lust, is not finished.")
            Wait.wait(1)
            print("DEMO FINISHED!")
            Score.score_calculate_and_save()
            #Saves the players score to Scoreboard.txt in the text folder
            print(f"YOU GOT {Score.total_score} POINTS!")
            #Shows how much scoret the player got
            Wait.wait(2)
            print("YOUR SCORE HAS BEEN SAVED TO 'Scoreboard.txt' IN THE 'text' FOLDER!")
            input("Press enter when you are ready to exit the game.")
            exit()

    #Placeholders for future levels that would be implimented in the full game
        elif circle == 3:
            print("Circle 3 - Gluttony, is not finished")

        elif circle == 4:
            print("Circle 4 - Greed, is not finished")

        elif circle == 5:
            print("Circle 5 - Wrath, is not finished")

        elif circle == 6:
            print("Circle 6 - Heresy, is not finished")

        elif circle == 7:
            print("Circle 7 - Violence, is not finished")

        elif circle == 8:
            print("Circle 8 - Fraud, is not finished")
            
        elif circle == 9:
            print("Circle 9 - Treachery, is not finished")

        else:
            print("ERROR")




elif endless_mode == True:
    Player.name = input("NAME: ")
    Wait.wait(1)
    while endless_mode == True:
        successful_encounter = True
        random_enemy = random.randint(1, 8)
        #Picks a random enemy and starts a combat encounter with them.
        if random_enemy == 1:
            Combat.standard_combat(Enemies.Filth.Name,
                                   Enemies.Filth.Health, 
                                   Enemies.Filth.Damage, 
                                   Enemies.Filth.Range,
                                   Enemies.Filth.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 2:
            Combat.standard_combat(Enemies.Stray.Name,
                                   Enemies.Stray.Health, 
                                   Enemies.Stray.Damage, 
                                   Enemies.Stray.Range,
                                   Enemies.Stray.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 3:
            Combat.standard_combat(Enemies.Schism.Name,
                                   Enemies.Schism.Health,
                                   Enemies.Schism.Damage, 
                                   Enemies.Schism.Range,
                                   Enemies.Schism.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 4:
            Combat.standard_combat(Enemies.Colossus.Name,
                                   Enemies.Colossus.Health,
                                   Enemies.Colossus.Damage, 
                                   Enemies.Colossus.Range,
                                   Enemies.Colossus.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 5:
            Combat.standard_combat(Enemies.Crawler.Name,
                                   Enemies.Crawler.Health, 
                                   Enemies.Crawler.Damage, 
                                   Enemies.Crawler.Range,
                                   Enemies.Crawler.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 6:
            Combat.standard_combat(Enemies.Guardian.Name,
                                   Enemies.Guardian.Health, 
                                   Enemies.Guardian.Damage, 
                                   Enemies.Guardian.Range,
                                   Enemies.Guardian.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 7:
            Combat.standard_combat(Enemies.Shade.Name,
                                   Enemies.Shade.Health, 
                                   Enemies.Shade.Damage, 
                                   Enemies.Shade.Range,
                                   Enemies.Shade.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 8:
            goose_chance = random.randint(1, 1000)
            if goose_chance == 852:
                Combat.standard_combat(Enemies.Goose.Name,
                                       Enemies.Goose.Health, 
                                       Enemies.Goose.Damage, 
                                       Enemies.Goose.Range,
                                       Enemies.Goose.Healing)
                endless_enemies_killed = endless_enemies_killed + 1
                successful_encounter = False
                #Very rare chance of fighting a goose
            else:
                pass
                successful_encounter = False
            #Easter egg encounter with a goose
            
        #Picks a random enemy from all avalible enemy types and adds to the
        #kill counter every time you win an ancounter

        if successful_encounter == True:
            #the post-fight parts only happen if the encounter wasnt an easter egg encounter
            print(f"{endless_enemies_killed} ENEMIES KILLED!")
            Wait.wait(1)

            if Weapons.chaingun_used == True:
                endless_chaingun_cooldown = endless_chaingun_cooldown + 1
                if endless_chaingun_cooldown == 5:
                    print_slow("CHAINGUN RESTORED!")
                    Weapons.chaingun_used = False
                    endless_chaingun_cooldown = 0
                else:
                    print(f"{5 - endless_chaingun_cooldown} KILLS UNTIL THE "
                          "CHAINGUN IS RESTORED")
                    Wait.wait(2)
                #If the chaingun has been used, after 5 kills it will be
                #restored
