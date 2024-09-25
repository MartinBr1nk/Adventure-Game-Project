#Imports
import time
import random
import Introduction
import Player
import Enemies
import Weapons


#Variables
name = "Placeholder"
direction = "placeholder"
prim_alt_choice = ""
choice_loop = False
skip = False
endless_mode = False
endless_enemies_killed = 0
endless_chaingun_cooldown = 0
loss = 0
alt_fire = "h"



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
    print_slow("THREAT DETECTED")
    print(f"{target_name} APPROACHES")
    print(f"{name} ATTACKS FIRST")
    time.sleep(1)
    combat_loop = True
    weapon_loop = True

    while combat_loop == True:
        #Puts you into a loop until you either lose or win
        print(f"{target_name} HAS {target_health} HP")
        time.sleep(1)

        while weapon_loop == True:
            #puts you in a loop until you pick a valid weapon
            print(f"""WEAPON CHOICES:
           1 - {Weapons.Revolver.Name} - {Weapons.Revolver.Info}
           2 - {Weapons.Shotgun.Name} - {Weapons.Shotgun.Info}
           3 - {Weapons.Chaingun.Name} - {Weapons.Chaingun.Info} """)
            weapon_choice = str(input("Choice: ")).lower()
            alt_fire = input("Use the alternate firing option? (Yes/No)").lower()
            if "n" in alt_fire:
                if weapon_choice == "1" or "revo" in weapon_choice and range <= Weapons.Revolver.Range:
                    target_health = target_health - int(Weapons.Revolver.Damage)
                    #If the weapon selected is equal to 1 AND the range is greater than or equal to the enemies range value, you attack
                    weapon_loop = False

                elif weapon_choice == "2" or "shot" in weapon_choice and range <= Weapons.Shotgun.Range:
                    target_health = target_health - int(Weapons.Shotgun.Damage)
                    #If the weapon selected is equal to 2 AND the range is greater than or equal to the enemies range value, you attack
                    weapon_loop = False

                elif weapon_choice == "3" or "chain" in weapon_choice and range <= Weapons.Chaingun.Range and Weapons.chaingun_used != True:
                    target_health = target_health - int(Weapons.Chaingun.Damage)
                    #If the weapon selected is equal to 3 AND the range is greater than or equal to the enemies range value AND the chaingun is functional, you attack
                    print("CHAINGUN USED, IT CANNOT BE USED AGAIN UNTIL REPAIRED")
                    Weapons.chaingun_used = True
                    weapon_loop = False

                elif weapon_choice == 3 and Weapons.chaingun_used == True:
                    print("THE CHAINGUN HAS ALREADY BEEN USED. YOU CANNOT USE IT AGAIN UNTIL YOU REPAIR IT.")
                    #prevents the chaingun from being used if it has already been used previously
                else:
                    print("PLEASE CHOOSE A VALID WEAPON WITH A SUITABLE RANGE. PICK THE NUMBER RELATED TO THE WEAPON.")
                    #In case the user enters a weapon that doesnt exist
            elif "y" in alt_fire:
                if weapon_choice == "1" or "revo" in weapon_choice:
                    target_health = target_health - int(Weapons.Revolver.Damage) * 2
                    Player.current_health = Player.current_health - 10
                    #If the weapon selected is equal to 1 AND the range is greater than or equal to the enemies range value, you attack
                    weapon_loop = False

                elif weapon_choice == "2" or "shot" in weapon_choice:
                    target_health = target_health - int(Weapons.Shotgun.Damage)
                    Player.current_health = Player.current_health - 50
                    #If the weapon selected is equal to 2 you shoot an infinite range shotgun projectile and take 50 damage
                    weapon_loop = False
            else:
                print("WEAPON HAS NO ALT FIRE/INVALID WEAPON")
                time.sleep(1)

        weapon_loop = True
        #sets weapon loop back to true so the next turn will work
        if Player.current_health <= 0:
            combat_loop = False
            print(f"{name} HAS RAN OUT OF FUEL.")
            time.sleep(2)
            death_screen()
            time.sleep(1)
            #Death :(

        elif target_health > 0:
            print(f"{target_name} HAS {target_health} HP")
            time.sleep(1)
            #Tells the player how much health the enemy has
            print(f"{target_name} ATTACKS!")
            time.sleep(1)
            print(f"{target_name} HITS AND CAUSES {name} TO LOSE {target_damage} FUEL.")
            time.sleep(1)
            Player.current_health = Player.current_health - target_damage
            print(f"{name} HAS {Player.current_health} FUEL REMAINING.")
            time.sleep(1)
            if Player.current_health <= 0:
                combat_loop = False
                print(f"{name} HAS RAN OUT OF FUEL.")
                time.sleep(2)
                death_screen()
                time.sleep(1)
                #Death :(

        elif target_health <= 0:
            print(f"{target_name} HAS DIED")
            time.sleep(2)
            Player.current_health = Player.current_health + healing
            Player.HealthCheck()
            print(f"{name} HAS {Player.current_health} FUEL REMAINING.")
            time.sleep(2)
            combat_loop = False
            print(f"{name} WINS.")
            time.sleep(1)
            #Victory!!! combat ends and the player heals, determined by the enemies healing factor.

        else:
            print("ERROR")
            exit()
            #debug message

def menu():
    global skip
    global endless_mode
    menu_loop = True
    while menu_loop == True:
        print(r"""
 __  __ ______ _   _ _    _ 
|  \/  |  ____| \ | | |  | |
| \  / | |__  |  \| | |  | |
| |\/| |  __| | . ` | |  | |
| |  | | |____| |\  | |__| |
|_|  |_|______|_| \_|\____/ 

1 - START CAMPAIGN
2 - ENDLESS FIGHTING MODE
3 - HOW TO PLAY (CHOOSE THIS ON A FIRST PLAYTHROUGH.)
4 - SETTINGS
5 - EXIT GAME

        """)
        try:
            menu_choice = int(input("WHERE DO YOU WANT TO NAVIGATE TO?: "))
            if menu_choice == 1:
                menu_loop = False
                time.sleep(3)
                clear_screen()

            elif menu_choice == 2:
                endless_mode = True
                menu_loop = False
                skip = True
                print("STARTING ENDLESS MODE")
                time.sleep(1)
                clear_screen()

            elif menu_choice == 3:
                print("UPPERCASE text passes automatically, it is spoken by machines")
                time.sleep(1)
                print("lowercase text must have you enter any key to continue. Try this now")
                input()
                print("Combat is turn based, firstly you take a turn and then the enemy takes their turn, as long as they are not dead.")
                input()
                print("The way you restore your fuel (Health) is by sucessfully killing enemies.")
                input()
                print("THIS IS THE ONLY WAY TO RESTORE FUEL.")
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

            elif menu_choice == 4:
                print("settings not finished")
                time.sleep(3)
                clear_screen()

            elif menu_choice == 5:
                print("CLOSING GAME...")
                exit()

            elif menu_choice == 9:
                print("skipping introduction!")
                skip = True
                menu_loop = False
                time.sleep(1)
                clear_screen()
            else:
                print("ENTER A VALID OPTION.")
                time.sleep(1)
        except:
            print("CHOSEN OPTION MUST BE A SINGLE NUMBER.")
        else:
            pass

random_value = random.randint(0, 500)
#Random Value generated at the start of every run that can cause special events to happen

menu()

game_loop = True
if endless_mode == False:

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

        if skip == False:
            Introduction.IntroSequence()
            name = Introduction.player_name
        else:
            name = "Pixel"
        print_slow(f"{name} IS APPROACHING... THE MOUTH OF HELL")
        print_slow("IMPACT IMMINENT...")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print_fast("IMPACT SUCCESSFUL")
        time.sleep(1)
        input("As the dust clears, you can see a way forward through a tunnel, obscured by smoke.")
        input("There are no other paths you can see. You decide to walk through the obscured tunnel")
        input("You reach a dark, open room with three locked doors to your left, right and directly in front of you.")
        time.sleep(1)

        combat(Enemies.Filth.Name, Enemies.Filth.Health, Enemies.Filth.Damage,\
               Enemies.Filth.Range, Enemies.Filth.Healing)
        #Gets the Name, Heath, Damage, Range and player healing for combat
        time.sleep(1)
        choice_loop = True
        while choice_loop == True:
            direction = input("The doors have unlocked, allowing you to progress either left, right or forward. :").lower()
            if direction == "left":
                choice_loop = False
                input("The door to your left slams open and allows you to pass through.")
                input("Ahead of you lies a long, cylindrical metal corridor.")
                input("The walls have been heated to an extreme temperature.")
                input("Suddenly...")
                print_slow("TRANSMISSION INCOMING...")
                time.sleep(1)

                input("A voice comes from the speakers in your suits cockpit:")
                input(f"'Hello {name}, this is a transmission from Headquarters.'")
                input("'It appears the Mouth of Hell has been overtaken by an unknown force,'")
                input("'We advise caution when attempting to -KZZZZZKT-'")
                print_slow("TRANSMISSION OVER.")

                combat(Enemies.Stray.Name, Enemies.Stray.Health, Enemies.Stray.Damage, \
                      Enemies.Stray.Range, Enemies.Stray.Healing)

            
                choice_loop = True
                input("The only way forward is to continue along the corridor, it doesnt appear that there are any more doors.")
                input("However, you could attempt to look around this room.")
                input("This may be dangerous as the walls of the room have been heated to an extreme temperature. ")
                while choice_loop == True:
                    #keeps the player in a loop until they make a valid choice.
                    choice = input("Inspect the Room? Yes/No: ").lower()
                    if "y" in choice:
                        input("You decide to inspect the room.")
                        print("!!! EXTREME HEAT DETECTED !!!")
                        time.sleep(2)
                        print("!!! ENGAGING COOLING MECHANISM !!!")
                        Player.current_health = Player.current_health - 100
                        time.sleep(2)
                        print(f"YOU HAVE LOST 100 OUT OF {Player.max_health} FUEL.")
                        print(f"YOU HAVE {Player.current_health} FUEL LEFT")
                        time.sleep(1)
                        input("You decide to continue along the corridor, as there does not appear to be anything else in this room")
                        choice_loop = False

                    elif "n" in choice:
                        input("You decide against inspecting the corridor.")
                        input("You continue along the corridor, as there does not appear to be anything else in this room")
                        choice_loop = False

                    else:
                        print("INVALID OPTION.")
                        time.sleep(1)

                input("Just as you left to the next room...")
                combat(Enemies.Schism.Name, Enemies.Schism.Health, Enemies.Schism.Damage,
                      Enemies.Schism.Range, Enemies.Schism.Healing)
                input("Ahead of you lies a crossroad, Door A appears to be the standard door with no differences to the other doors you have been passing through.")
                input("Door B has an 'EXIT' sign above it, it seems to be damaged and would require a lot of force to break through.")
                input("If you want to get through door B you will have to spend 25 - 100 fuel to smash through it.")
                choice_loop = True
                if choice_loop == True:
                    choice = input("Smash through the door?").lower()

                    if "y" in choice:
                        print_slow("PREPARING TO DESTROY DOOR")
                        loss = random.randint(25, 100)
                        Player.current_health = Player.current_health - loss

                        if Player.current_health <= 0:
                            print_slow("FUEL AT CRITICAL LEVELS")
                            print_slow("POWERING DOWN...")
                            death_screen()

                        else:
                            print_slow("ATTEMPT SUCCESSFUL")
                            print(f"{loss} FUEL LOST IN THE PROCESS. YOU HAVE {Player.current_health} FUEL LEFT")
                            time.sleep(1)
                        input("Behind the door is a large chasm in the ground, there appears to be a path to your left that may be connected to the path that Door A would take you to. You can see the shadow of a massive husk from this path.")
                        input("Suddenly...")
                        print_slow("PATH AHEAD DETECTED")
                        input("Your suit suddenly begins walking towards the chasm and prepares to jump in")
                        input("The suit controls have been taken over by the suits AI, you cannot prevent its decent.")
                        print_slow("BEGINNING DECENT...")
                        #Put exit code here once I finish The Mouth of Hell

                    elif "n" in choice:
                        input("You decide to take the standard door around")
                        input("Ahead of you lies a corridor filled with enemies, and at the end you can see a right turn that would lead you to where Door B is connected to.")

                        combat(Enemies.Stray.Name, Enemies.Stray.Health, Enemies.Stray.Damage, \
                            Enemies.Stray.Range, Enemies.Stray.Healing)

                        combat(Enemies.Filth.Name, Enemies.Filth.Health, Enemies.Filth.Damage, \
                            Enemies.Filth.Range, Enemies.Filth.Healing)

                        combat(Enemies.Schism.Name, Enemies.Schism.Health, Enemies.Schism.Damage, \
                            Enemies.Schism.Range, Enemies.Schism.Healing)

                        print_slow("LARGE ENEMY AHEAD, PREPARE YOURSELF")
                        combat(Enemies.Colossus.Name, Enemies.Colossus.Health, Enemies.Colossus.Damage, \
                            Enemies.Colossus.Range, Enemies.Colossus.Healing)

                        input("Behind the turning is a large chasm in the ground, there appears to be a door to your right that is connected to the path that Door B would take you to.")
                        input("Suddenly...")
                        print_slow("PATH AHEAD DETECTED")
                        input("Your suit suddenly begins walking towards the chasm and prepares to jump in")
                        input("The suit controls have been taken over by the suits AI, you cannot prevent its decent.")
                        print_slow("BEGINNING DECENT...")
                        #Put exit code here once I finish The Mouth of Hell
                    else:
                        print("INVALID OPTION")
                        time.sleep(1)

            elif direction == "right":
                choice_loop = False
                input("The door to your right slams closed behind you, ahead of you lies a fork in the road with doors to the left and right.")
                input("Suddenly...")
                print_slow("TRANSMISSION INCOMING...")
                time.sleep(1)

                input("A voice comes from the speakers in your suits cockpit:")
                input(f"'Hello {name}, this is a transmission from Headquarters.'")
                input("'It appears the Mouth of Hell has been overtaken by an unknown force,'")
                input("'We advise caution when attempting to -KZZZZZKT-'")
                print_slow("TRANSMISSION OVER.")
                combat(Enemies.Filth.Name, Enemies.Filth.Health, Enemies.Filth.Damage,\
                       Enemies.Filth.Range, Enemies.Filth.Healing)

                choice_loop = True
                input("There is a door to your left and a door to your right")
                while choice_loop == True:
                    choice = input("Do you go left or right?: ")
                    if "l" in choice:
                        choice_loop = False
                        input("You enter a long corridoor, with a large enemy blocking the path forward.")
                        input("You can see a potential exit ahead")
                        input("Suddenly...")
                        combat(Enemies.Colossus.Filth.Name, Enemies.Colossus.Health, Enemies.Colossus.Damage,\
                                Enemies.Colossus.Range, Enemies.Colossus.Healing)
                        input("You continue ahead through the corridoor and reach a chasm in the ground")
                        print_slow("PATH AHEAD DETECTED")
                        print_slow("BEGINNING DECENT...")
                        #Put exit code here once I finish The Mouth of Hell
                    elif "r" in choice:
                        choice_loop = False
                        input("You enter a room resembling a cavern with no way through.")
                        input("You could explore the room to check if anything")
                        choice_loop = True
                        while choice_loop == True:
                            choice = input("Explore the room?: ").lower()
                            if "y" in choice:
                                choice_loop = False
                                input("You find a small lever hidden amongst the rocks in the room.")
                                input("You decide to pull the lever.")
                                input("The ground beneath you suddenly begins to open into a chasm")
                                print_slow("PATH AHEAD DETECTED")
                                print_slow("BEGINNING DECENT...")
                                #Put exit code here once I finish The Mouth of Hell
                                break
                            elif "n" in choice:
                                choice_loop = False
                                input("Suddenly...")
                                print_slow("Something wicked this way comes")
                                combat(Enemies.SomethingWicked.Name, Enemies.SomethingWicked.Health, Enemies.SomethingWicked.Damage, \
                                       Enemies.SomethingWicked.Range, Enemies.SomethingWicked.Healing)
                                #starts a easter egg fight that is impossible to win
                            else:
                                print("PLEASE CHOOSE A VALID OPTION.")
                    else:
                        print("PICK A VALID OPTION.")

            elif direction == "forward":
                choice_loop = False
                input("The door ahead of you slams open allowing you to continue forward.")
                input("The room behind the door is a large, winding staircase above a massive spinning fan, falling would result in instant death")
                input("Suddenly...")
                print_slow("TRANSMISSION INCOMING...")
                time.sleep(1)

                input("A voice comes from the speakers in your suits cockpit:")
                input(f"'Hello {name}, this is a transmission from Headquarters.'")
                input("'It appears the Mouth of Hell has been overtaken by an unknown force,'")
                input("'We advise caution when attempting to -KZZZZZKT-'")
                print_slow("TRANSMISSION OVER.")

                input("You can see many enemies lying on the staircase")
                input("if you use a charge of your chaingun you may be able to destroy the floor beneath some of the enemies.")
                if choice_loop == True:
                    choice = input("Do you use your chaingun?: ").lower()
                    if "y" in choice:
                        choice_loop = False
                        Weapons.chaingun_used = True
                        print("CHAINGUN USED, IT CANNOT BE USED AGAIN UNTIL REPAIRED")
                        time.sleep(1)
                        input("The staircase ahead crumbles infront of you, leaving a massive gap that you need to cross.")
                        input("However, all the enemies that you would have had to fought have fell and been shredded by the fan beneath.")
                        input("There is a huge gap between you and the next door.")
                        input("You'll have to jump the gap.")
                        input("To successfully jump the gap you will have to use HALF of your fuel to make the jump.")
                        input("You could risk it and lose only a third of your fuel to jump the gap but there is a chance you may fall and be shredded.")
                        choice_loop = True
                        while choice_loop == True:
                            choice = input("Play it safe and use half your fuel to jump the gap?: ").lower()
                            if "y" in choice:
                                choice_loop = False
                                Player.current_health = Player.current_health / 2
                                print(f"{Player.current_health} FUEL REMAINING.")
                                time.sleep(1)
                            elif "n" in choice:
                                choice_loop = False
                                input("You brace yourself to jump.")
                                jump_risk = random.randint(1, 5)
                                if jump_risk == 1:
                                    print_slow("JUMP FAILED")
                                    time.sleep(1)
                                    print_slow("EMERGENCY EJ-")
                                    death_screen()
                                else:
                                    Player.current_health = Player.current_health / 1.3
                                    print(f"{Player.current_health} FUEL REMAINING.")
                                    time.sleep(1)
                            input("You have successfuly jumped the gap.")
                            input("The door at the end slams open and you can see a chasm that drops down for a indeterminate distance.")
                            input("Suddenly...")
                            print_slow("PATH AHEAD DETECTED")
                            input("Your suit suddenly begins walking towards the chasm and prepares to jump in")
                            input("The suit controls have been taken over by the suits AI, you cannot prevent its decent.")
                            print_slow("BEGINNING DECENT...")
                            #Put exit code here once I finish The Mouth of Hell
                    elif "n" in choice:
                        choice_loop = False
                        input("You decide against using the chaingun.")
                        input("You'll have to fight through several tough enemies to get through now.")
                        combat(Enemies.Stray.Name, Enemies.Stray.Health, Enemies.Stray.Damage, \
                            Enemies.Stray.Range, Enemies.Stray.Healing)
                        combat(Enemies.Stray.Name, Enemies.Stray.Health, Enemies.Stray.Damage, \
                            Enemies.Stray.Range, Enemies.Stray.Healing)
                        combat(Enemies.Schism.Name, Enemies.Schism.Health, Enemies.Schism.Damage, \
                            Enemies.Schism.Range, Enemies.Schism.Healing)
                        print_slow("GIANT ENEMY AHEAD.")
                        combat(Enemies.Colossus.Name, Enemies.Colossus.Health, Enemies.Colossus.Damage, \
                            Enemies.Colossus.Range, Enemies.Colossus.Healing)
                        input("You can now continue further.")

                        input("The door at the end slams open and you can see a chasm that drops down for a indeterminate distance.")
                        input("Suddenly...")
                        print_slow("PATH AHEAD DETECTED")
                        input("Your suit suddenly begins walking towards the chasm and prepares to jump in")
                        input("The suit controls have been taken over by the suits AI, you cannot prevent its decent.")
                        print_slow("BEGINNING DECENT...")
                        #Put exit code here once I finish The Mouth of Hell
                        
                    else:
                        print("INVALID OPTION.")
                        print("\n")
                        time.sleep(1)

            else:
                print("PICK A VALID DIRECTION.")
                time.sleep(1)




elif endless_mode == True:
    name = input("NAME: ")
    time.sleep(1)

    while endless_mode == True:
        random_enemy = random.randint(1, 4)
        if random_enemy == 1:
            combat(Enemies.Filth.Name, Enemies.Filth.Health, Enemies.Filth.Damage, \
               Enemies.Filth.Range, Enemies.Filth.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 2:
            combat(Enemies.Stray.Name, Enemies.Stray.Health, Enemies.Stray.Damage, \
               Enemies.Stray.Range, Enemies.Stray.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 3:
            combat(Enemies.Schism.Name, Enemies.Schism.Health, Enemies.Schism.Damage, \
               Enemies.Schism.Range, Enemies.Schism.Healing)
            endless_enemies_killed = endless_enemies_killed + 1

        elif random_enemy == 4:
            combat(Enemies.Colossus.Name, Enemies.Colossus.Health, Enemies.Colossus.Damage, \
               Enemies.Colossus.Range, Enemies.Colossus.Healing)
            endless_enemies_killed = endless_enemies_killed + 1
        #Picks a random enemy from all avalible enemy types

        print(f"{endless_enemies_killed} ENEMIES KILLED!")
        time.sleep(1)

        if Weapons.chaingun_used == True:
            endless_chaingun_cooldown = endless_chaingun_cooldown + 1
            if endless_chaingun_cooldown == 5:
                print_slow("CHAINGUN RESTORED!")
                Weapons.chaingun_used = False
            else:
                print(f"{5 - endless_chaingun_cooldown} KILLS UNTIL THE CHAINGUN IS RESTORED")
                time.sleep(2)
            #If the chaingun has been used, after 5 kills it will be restored

#end