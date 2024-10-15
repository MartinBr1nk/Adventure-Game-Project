import ASCII
import Wait
import Score
from Terminal import terminal

def clear_screen():
    for clear_x in range(50):
        print("\n")
        #"Clears" the screen by pushing everything else away


def menu():
    global skip
    global endless_mode
    global circle
    global through_menu
    menu_loop = True
    while menu_loop == True:
        print(ASCII.menu_title, r"""

1 - START CAMPAIGN
2 - ENDLESS FIGHTING MODE
3 - HOW TO PLAY
4 - SETTINGS
5 - VIEW SCOREBOARD
6 - VIEW TERMINAL
7 - EXIT GAME

        """)
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
                #Starts the game
            elif "1" in menu_choice or "limbo" in menu_choice:
                menu_loop = False
                through_menu = True
                circle = 1
                Wait.wait(3)
                clear_screen()
                #Starts the game
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
            #Prints tutorial.

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
            elif "2" in setting_choice or "wipe" in setting_choice:
                setting_choice = input("Are you sure you want to wip the "
                                       "scoreboard? This CANNOT BE "
                                       "REVERSED. Type YES in UPPERCASE "
                                       "LETTERS if you are CERTAIN you want "
                                       "to wipe the scoreboard.: ")
                if "YES" in setting_choice:
                    Score.scoreboard_wipe()
                else:
                    print("WIPE ABORTED.")

                print("SCOREBOARD WIPED!")
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

        elif "6" in menu_choice or "terminal" in menu_choice:
            clear_screen()
            terminal()
            clear_screen()

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