import time
import random
import ASCII
import Wait
import Player

def cool_typing(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.1, 0.05))
    print("\n")

def cool_typing_fast(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.0005, 0.0001))
    print("\n")

def death_screen():
    cool_typing_fast(ASCII.death_screen)
    exit()
    #different death screen because I cant circular import:(


def IntroSequence():
    cool_typing("BOOT UP SEQUENCE READY")
    cool_typing("CHECKING FIRMWARE VERISON")
    print("LATEST VERSION (15.09.2163)")
    Wait.wait(1)

    print("PEFORMING SYSTEM DIAGNOSTICS")
    cool_typing("AUDIO             OK")
    cool_typing("VIDEO FEED        ERROR")
    cool_typing("MECHANICS         OK")
    print("DUE TO VIDEO FEED MALFUNCTION, PLEASE NOTE YOUR ENVIROMENT "
          "AS YOU PROCEED")
    Wait.wait(3)

    print("DIAGNOSTIC COMPLETE")
    Wait.wait(3)

    print("PLEASE ENTER A NAME SO YOUR CADEVER CAN BE IDENTIFIED")
    Wait.wait(2)
    Player.name = input("PILOT NAME: ")
    if "skibidi" in Player.name.lower() or "gyatt" in Player.name.lower() \
       or "rizz" in Player.name.lower() or "sigma" in Player.name.lower() \
       or "ohio" in Player.name.lower() or "hawk" in Player.name.lower() \
       or "tuah" in Player.name.lower() or "aura" in Player.name.lower() \
       or "fanum" in Player.name.lower() or "alpha" in Player.name.lower() \
       or "mew" in Player.name.lower() or "mog" in Player.name.lower() \
       or "gronk" in Player.name.lower() or "glazing" in Player.name.lower() \
       or "cenat" in Player.name.lower():
        #if these terms are within your name,
        #the game just kills you before you can start.
        cool_typing("RELEASING TOXIC GAS...")
        Wait.wait(3)
        cool_typing("BRAINROT IS NOT PERMITTED IN THE HELL "
                   "EXPEDITION PROJECT.")
        Wait.wait(1)
        death_screen()

    elif "gaster" in Player.name.lower():
        cool_typing("VERY VERY INTRESTING.")
        Player.name = "W.D Gaster"
        #Easter egg that references another game

    elif "mykola" in Player.name.lower():
        Player.name = ASCII.Mykolasaurus
        Wait.time_skip = True
        #stupid inside joke

    elif "silly" in Player.name.lower():
        Player.name = ASCII.silly_cat
        Wait.time_skip = True
        #stupid easter egg

    elif "farming" in Player.name.lower() or "martin" in Player.name.lower():
        cool_typing("FARMING MODE INITIATED.")
        Wait.wait(1)
        cool_typing("LOADING.................")
        Wait.wait(5)
        print("just kidding :) it broke.")
        #Easter egg (farming didnt actually break, I never programmed it)
        Wait.wait(3)

    elif Player.name == "":
        Wait.wait(1)
        Player.name = input("PLEASE ENTER A NAME, OR ONE WILL BE "
                            "CHOSEN FOR YOU: ")
        if Player.name == "":
            Player.name = "PILOT"
            Wait.wait(1)
            print(f"SET NAME - {Player.name}.")
            Wait.wait(1)
            #Picks a default name if the user does not enter anything.
        else:
            print(f"SET NAME - {Player.name}.")
            Wait.wait(1)
    else:
        print(f"SET NAME - {Player.name}.")

    Player.name = Player.name

    cool_typing("STATUS UPDATE - APPROACHING HELL")