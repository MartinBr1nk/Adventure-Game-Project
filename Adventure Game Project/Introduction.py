import time
import random

def CoolTyping(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.3, 0.05))
    print("\n")

def IntroSequence():
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
    if PlayerName == "":
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