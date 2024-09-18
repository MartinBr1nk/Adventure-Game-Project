import time
import random

def CoolTyping(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.1, 0.05))
    print("\n")

def CoolTyping_fast(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.0005, 0.0001))
    print("\n")

def DeathScreen():
    CoolTyping_fast("""
    
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
    global PlayerName
    CoolTyping("BOOT UP SEQUENCE READY")
    CoolTyping("CHECKING FIRMWARE VERISON")
    print("LATEST VERSION (15.09.2163)")
    time.sleep(1)
    print("PEFORMING SYSTEM DIAGNOSTICS")
    CoolTyping("AUDIO             OK")
    CoolTyping("VIDEO FEED        ERROR")
    CoolTyping("MECHANICS         OK")
    print("DUE TO VIDEO FEED MALFUNCTION, PLEASE NOTE YOUR ENVIROMENT AS YOU PROCEED")
    time.sleep(3)
    print("DIAGNOSTIC COMPLETE")
    time.sleep(3)

    print("PLEASE ENTER A NAME SO YOUR CADEVER CAN BE IDENTIFIED")
    time.sleep(2)
    PlayerName = input("PILOT NAME: ")
    if "skibidi" in PlayerName.lower() or "gyatt" in PlayerName.lower() or "rizz" in PlayerName.lower() or "sigma" in PlayerName.lower() or "ohio" in PlayerName.lower() or "hawk" in PlayerName.lower() or "tuah" in PlayerName.lower() or "aura" in PlayerName.lower() or "fanum" in PlayerName.lower() or "alpha" in PlayerName.lower() or "mew" in PlayerName.lower() or "mog" in PlayerName.lower() or "gronk" in PlayerName.lower() or "glazing" in PlayerName.lower() or "cenat" in PlayerName.lower():
        #if these terms are within your name, the game just kills you before you can start.
        CoolTyping("RELEASING TOXIC GAS...")
        time.sleep(3)
        CoolTyping("BRAINROT IS NOT PERMITTED IN THE HELL EXPEDITION PROJECT.")
        time.sleep(1)
        DeathScreen()

    elif PlayerName == "":
        time.sleep(1)
        PlayerName = input("PLEASE ENTER A NAME, OR ONE WILL BE CHOSEN FOR YOU: ")
        if PlayerName == "":
            PlayerName = f"PILOT-{random.randint(1, 999999)}"
            time.sleep(1)
            print(f"SET NAME - {PlayerName}.")
            time.sleep(1)

        else:
            PlayerName = f"{PlayerName}-{random.randint(1, 999999)}"
            print(f"SET NAME - {PlayerName}.")
            time.sleep(1)
    else:
        PlayerName = f"{PlayerName}-{random.randint(1, 999999)}"
        print(f"SET NAME - {PlayerName}.")

    CoolTyping("STATUS UPDATE - APPROACHING HELL")