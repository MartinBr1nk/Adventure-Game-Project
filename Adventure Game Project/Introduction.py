import time
import random

def cool_typing(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.1, 0.05))
    print("\n")

def cool_typing_fast(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.0005, 0.0001))
    print("\n")

def death_screen():
    cool_typing_fast("""
    
__   _______ _   _  ______ _____ ___________ 
\ \ / /  _  | | | | |  _  \_   _|  ___|  _  |
 \ V /| | | | | | | | | | | | | | |__ | | | |
  \ / | | | | | | | | | | | | | |  __|| | | |
  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ / 
  \_/  \___/ \___/  |___/  \___/\____/|___/  
    
    """)
    exit()
    #different death screen because I cant circular import:(


def IntroSequence():
    global player_name
    cool_typing("BOOT UP SEQUENCE READY")
    cool_typing("CHECKING FIRMWARE VERISON")
    print("LATEST VERSION (15.09.2163)")
    time.sleep(1)

    print("PEFORMING SYSTEM DIAGNOSTICS")
    cool_typing("AUDIO             OK")
    cool_typing("VIDEO FEED        ERROR")
    cool_typing("MECHANICS         OK")
    print("DUE TO VIDEO FEED MALFUNCTION, PLEASE NOTE YOUR ENVIROMENT AS YOU PROCEED")
    time.sleep(3)

    print("DIAGNOSTIC COMPLETE")
    time.sleep(3)

    print("PLEASE ENTER A NAME SO YOUR CADEVER CAN BE IDENTIFIED")
    time.sleep(2)
    player_name = input("PILOT NAME: ")
    if "skibidi" in player_name.lower() or "gyatt" in player_name.lower() \
       or "rizz" in player_name.lower() or "sigma" in player_name.lower() \
       or "ohio" in player_name.lower() or "hawk" in player_name.lower() \
       or "tuah" in player_name.lower() or "aura" in player_name.lower() \
       or "fanum" in player_name.lower() or "alpha" in player_name.lower() \
       or "mew" in player_name.lower() or "mog" in player_name.lower()\
       or "gronk" in player_name.lower() or "glazing" in player_name.lower()\
       or "cenat" in player_name.lower():
        #if these terms are within your name, the game just kills you before you can start.
        cool_typing("RELEASING TOXIC GAS...")
        time.sleep(3)
        cool_typing("BRAINROT IS NOT PERMITTED IN THE HELL EXPEDITION PROJECT.")
        time.sleep(1)
        death_screen()

    elif "gaster" in player_name.lower():
        cool_typing("VERY VERY INTRESTING.")
        player_name = "W.D Gaster"

    elif "farming" in player_name.lower() or "martin" in player_name.lower():
        cool_typing("FARMING MODE INITIATED.")
        time.sleep(1)
        cool_typing("LOADING.................")
        time.sleep(5)
        print("just kidding :)")
        time.sleep(3)

    elif player_name == "":
        time.sleep(1)
        player_name = input("PLEASE ENTER A NAME, OR ONE WILL BE CHOSEN FOR YOU: ")
        if player_name == "":
            player_name = "PILOT"
            time.sleep(1)
            print(f"SET NAME - {player_name}.")
            time.sleep(1)
        else:
            print(f"SET NAME - {player_name}.")
            time.sleep(1)
    else:
        print(f"SET NAME - {player_name}.")

    cool_typing("STATUS UPDATE - APPROACHING HELL")