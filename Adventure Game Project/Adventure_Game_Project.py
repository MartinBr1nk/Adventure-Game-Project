#Imports
import time
import random
import Introduction
import Player
import Enemies
import Weapons

Name = "Placeholder"
#functions

            

def Save(ValueName, Value):
    f = open("SaveData.py", "a")
    f.write(str(ValueName) + " = " + str(Value) + "\n")
    f.close()
    #useless saving system, it doesnt really work for what I want but I'm leaving it in in case I need it later

def print_slow(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.1, 0.05))
    print("\n")

def print_fast(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.0005, 0.0001))
    print("\n")


def DeathScreen():
    print_fast("""
    
__   _______ _   _  ______ _____ ___________ 
\ \ / /  _  | | | | |  _  \_   _|  ___|  _  |
 \ V /| | | | | | | | | | | | | | |__ | | | |
  \ / | | | | | | | | | | | | | |  __|| | | |
  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ / 
  \_/  \___/ \___/  |___/  \___/\____/|___/  
    
    """)
    exit()
    #Death screen

def Combat(TargetName, TargetHealth, TargetDamage, Range, Healing): #add range before healing
    print(f"{TargetName} APPROACHES")
    print(f"{Name} ATTACKS FIRST")
    time.sleep(1)
    CombatLoop = True

    while CombatLoop == True:
        #Puts you into a loop until you either lose or win
        print(f"{TargetName} HAS {TargetHealth} HP")
        time.sleep(1)
        print(f"""WEAPON CHOICES:
       1 - {Weapons.Revolver.Name} - {Weapons.Revolver.Info}
       2 - {Weapons.Shotgun.Name} - {Weapons.Shotgun.Info}
       3 - {Weapons.Chaingun.Name} - {Weapons.Chaingun.Info} """)
        time.sleep(1)
        WeaponChoice = int(input("Choice: "))

        if WeaponChoice == 1 and Range <= Weapons.Revolver.Range:
            TargetHealth = TargetHealth - int(Weapons.Revolver.Damage)
            #If the weapon selected is equal to 1 AND the range is greater than or equal to the enemies range value, you attack

        elif WeaponChoice == 2 and Range <= Weapons.Shotgun.Range:
            TargetHealth = TargetHealth - int(Weapons.Shotgun.Damage)
            #If the weapon selected is equal to 2 AND the range is greater than or equal to the enemies range value, you attack

        elif WeaponChoice == 3 and Range <= Weapons.Chaingun.Range and Weapons.ChaingunUsed != True:
            TargetHealth = TargetHealth - int(Weapons.Chaingun.Damage)
            #If the weapon selected is equal to 3 AND the range is greater than or equal to the enemies range value AND the chaingun is functional, you attack
            print("CHAINGUN USED, IT CANNOT BE USED AGAIN UNTIL REPAIRED")
            Weapons.ChaingunUsed = True

        elif WeaponChoice == 3 and Weapons.ChaingunUsed == True:
            print("THE CHAINGUN HAS ALREADY BEEN USED. YOU CANNOT USE IT AGAIN UNTIL YOU REPAIR IT.")
            #prevents the chaingun from being used if it has already been used previously

        else:
            print("PLEASE CHOOSE A VALID WEAPON WITH A SUITABLE RANGE. PICK THE NUMBER RELATED TO THE WEAPON.")
            #In case the user enters a weapon that doesnt exist

        print(f"{TargetName} HAS {TargetHealth} HP")
        #Tells the player how much health the enemy has
        print(f"{TargetName} ATTACKS!")
        print(f"{TargetName} HITS AND CAUSES YOU TO LOSE {TargetDamage} FUEL.")
        Player.CurrentHealth = Player.CurrentHealth - TargetDamage
        print(f"YOU HAVE {Player.CurrentHealth} FUEL REMAINING.")

        if TargetHealth < 0:
            print(f"{TargetName} HAS DIED")
            Player.CurrentHealth = Player.CurrentHealth + Healing
            Player.HealthCheck()
            print(f"YOU HAVE {Player.CurrentHealth} HEALTH REMAINING.")
            CombatLoop = False
            #Victory!!! combat ends and the player heals, determined by the enemies healing factor.
        elif Player.CurrentHealth <= 0:
            CombatLoop = False
            print(f"YOU HAVE RAN OUT OF FUEL.")
            DeathScreen()
            time.sleep(1)
            #Death :(


RandomVal = random.randint(0, 500)
#Random Value generated at the start of every run that can cause special events to happen

GameLoop = True

while GameLoop == True:
    print_fast(r"""
    
 _____ _   _  _____   _   _  _____ _      _                   
|_   _| | | ||  ___| | | | ||  ___| |    | |                  
  | | | |_| || |__   | |_| || |__ | |    | |                  
  | | |  _  ||  __|  |  _  ||  __|| |    | |                  
  | | | | | || |___  | | | || |___| |____| |____              
  \_/ \_| |_/\____/  \_| |_/\____/\_____/\_____/              
 _______   ________ ___________ _____ _____ _____ _____ _   _ 
|  ___\ \ / /| ___ \  ___|  _  \_   _|_   _|_   _|  _  | \ | |
| |__  \ V / | |_/ / |__ | | | | | |   | |   | | | | | |  \| |
|  __| /   \ |  __/|  __|| | | | | |   | |   | | | | | | . ` |
| |___/ /^\ \| |   | |___| |/ / _| |_  | |  _| |_\ \_/ / |\  |
\____/\/   \/\_|   \____/|___/  \___/  \_/  \___/ \___/\_| \_/        
____________ _____   ___ _____ _____ _____                    
| ___ \ ___ \  _  | |_  |  ___/  __ \_   _|                   
| |_/ / |_/ / | | |   | | |__ | /  \/ | |                     
|  __/|    /| | | |   | |  __|| |     | |                     
| |   | |\ \\ \_/ /\__/ / |___| \__/\ | |                     
\_|   \_| \_|\___/\____/\____/ \____/ \_/                     

    """)

    
    Introduction.IntroSequence()
    Name = Introduction.PlayerName

    print_slow("THE PILOT IS APPROACHING... THE MOUTH OF HELL")

