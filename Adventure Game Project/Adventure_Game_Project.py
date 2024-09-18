#Imports
import time
import random
import Introduction
import Player
import Enemies
import Weapons

name = "Placeholder"
direction = "placeholder"
#functions
def clear_screen():
    for x in range(25):
        print("\n")

def save(ValueName, Value):
    f = open("SaveData.py", "a")
    f.write(str(ValueName) + " = " + str(Value) + "\n")
    f.close()
    #useless saving system, it doesnt really work for what I want but I'm leaving it in in case I need it later

def print_slow(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.1, 0.05))
    print("\n")
    #prints text letter-by-letter slowly

def print_fast(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.0005, 0.0001))
    print("\n")
    #prints text letter-by-letter quickly

def print_REALLY_fast(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.000005, 0.000001))
    print("\n")
    #prints text letter-by-letter REALLY quickly

def death_screen():
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

def combat(target_name, target_health, target_damage, range, healing):
    print(f"{target_name} APPROACHES")
    print(f"{name} ATTACKS FIRST")
    time.sleep(1)
    CombatLoop = True

    while CombatLoop == True:
        #Puts you into a loop until you either lose or win
        print(f"{target_name} HAS {target_health} HP")
        time.sleep(1)
        print(f"""WEAPON CHOICES:
       1 - {Weapons.Revolver.Name} - {Weapons.Revolver.Info}
       2 - {Weapons.Shotgun.Name} - {Weapons.Shotgun.Info}
       3 - {Weapons.Chaingun.Name} - {Weapons.Chaingun.Info} """)
        time.sleep(1)
        WeaponChoice = int(input("Choice: "))

        if WeaponChoice == 1 and range <= Weapons.Revolver.Range:
            target_health = target_health - int(Weapons.Revolver.Damage)
            #If the weapon selected is equal to 1 AND the range is greater than or equal to the enemies range value, you attack

        elif WeaponChoice == 2 and range <= Weapons.Shotgun.Range:
            target_health = target_health - int(Weapons.Shotgun.Damage)
            #If the weapon selected is equal to 2 AND the range is greater than or equal to the enemies range value, you attack

        elif WeaponChoice == 3 and range <= Weapons.Chaingun.Range and Weapons.chaingun_used != True:
            target_health = target_health - int(Weapons.Chaingun.Damage)
            #If the weapon selected is equal to 3 AND the range is greater than or equal to the enemies range value AND the chaingun is functional, you attack
            print("CHAINGUN USED, IT CANNOT BE USED AGAIN UNTIL REPAIRED")
            Weapons.chaingun_used = True

        elif WeaponChoice == 3 and Weapons.chaingun_used == True:
            print("THE CHAINGUN HAS ALREADY BEEN USED. YOU CANNOT USE IT AGAIN UNTIL YOU REPAIR IT.")
            #prevents the chaingun from being used if it has already been used previously

        else:
            print("PLEASE CHOOSE A VALID WEAPON WITH A SUITABLE RANGE. PICK THE NUMBER RELATED TO THE WEAPON.")
            #In case the user enters a weapon that doesnt exist


        if target_health < 0:
            print(f"{target_name} HAS DIED")
            time.sleep(2)
            Player.current_health = Player.current_health + healing
            Player.HealthCheck()
            print(f"YOU HAVE {Player.current_health} FUEL REMAINING.")
            time.sleep(2)
            CombatLoop = False
            #Victory!!! combat ends and the player heals, determined by the enemies healing factor.
        elif Player.current_health <= 0:
            CombatLoop = False
            print(f"YOU HAVE RAN OUT OF FUEL.")
            time.sleep(2)
            death_screen()
            time.sleep(1)
            #Death :(
        else:
            print(f"{target_name} HAS {target_health} HP")
            time.sleep(1)
            #Tells the player how much health the enemy has
            print(f"{target_name} ATTACKS!")
            time.sleep(1)
            print(f"{target_name} HITS AND CAUSES YOU TO LOSE {target_damage} FUEL.")
            time.sleep(1)
            Player.current_health = Player.current_health - target_damage
            print(f"YOU HAVE {Player.current_health} FUEL REMAINING.")
            time.sleep(1)
            print(f"YOU WIN.")
            time.sleep(1)

def menu():
    MenuLoop = True
    while MenuLoop == True:
        print(r"""
 __  __ ______ _   _ _    _ 
|  \/  |  ____| \ | | |  | |
| \  / | |__  |  \| | |  | |
| |\/| |  __| | . ` | |  | |
| |  | | |____| |\  | |__| |
|_|  |_|______|_| \_|\____/ 

1 - START GAME
2 - HOW TO PLAY (CHOOSE THIS ON A FIRST PLAYTHROUGH.)
3 - SETTINGS
4 - EXIT GAME

        """)
        try:
            Choice = int(input("WHERE DO YOU WANT TO NAVIGATE TO?: "))
            if Choice == 1:
                MenuLoop = False
                time.sleep(3)
                clear_screen()
            elif Choice == 2:
                print("UPPERCASE text passes automatically")
                time.sleep(1)
                print("lowercase text must have you enter any key to continue. Try this now")
                input()
                print("Combat is turn based, firstly you take a turn and then the enemy takes their turn, as long as they are not dead.")
                input()
                print("The way you restore your fuel (Health) is by sucessfully killing enemies.")
                input()
                print("THIS IS THE ONLY WAY TO RESTORE HP.")
                time.sleep(1)
                print("Stronger enemies restore more fuel, while weaker enemies will restore less fuel")
                input()
                print("Every path in the game will eventually lead to an exit. Every way forward will lead to progress.")
                input()
                print("This doesnt mean that some paths will be easy, each path will have their own challenges and secrets that you can discover and overcome.")
                input()
                print("Press any key when you are ready to return to the menu")
                input()
                clear_screen()
            elif Choice == 3:
                print("settings not finished")
                time.sleep(3)
                clear_screen()
            elif Choice == 4:
                print("CLOSING GAME...")
                exit()
            else:
                print("ENTER A VALID OPTION.")
                time.sleep(1)
        except:
            print("CHOSEN OPTION MUST BE A SINGLE INTEGER.")
        else:
            pass


random_value = random.randint(0, 500)
#Random Value generated at the start of every run that can cause special events to happen

menu()

game_loop = True

while game_loop == True:
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
    name = Introduction.PlayerName

    print_slow("THE PILOT IS APPROACHING... THE MOUTH OF HELL")
    print_slow("IMPACT IMMINENT...")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print_fast("IMPACT SUCCESSFUL")
    time.sleep(1)
    input("As the dust clears, you can see a way forward through a tunnel, obscured by smoke and soot.")
    input("There are no other paths you can see. You decide to walk through the obscured tunnel")
    input("You reach a dark, open room with three locked doors to your left, right and directly in front of you.")
    time.sleep(1)
    print_slow("THREAT DETECTED")

    combat(Enemies.Filth.Name, Enemies.Filth.Health, Enemies.Filth.Damage, Enemies.Filth.Damage, Enemies.Filth.Healing)
    time.sleep(1)

    direction = input("The doors have unlocked, allowing you to progress either left, right or forward. :")


