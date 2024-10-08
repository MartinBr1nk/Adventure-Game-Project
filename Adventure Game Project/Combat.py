import Wait
import ASCII
import Player
import random
import Weapons

def print_slow(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.1, 0.05))
    print("\n")
    #prints text letter-by-letter slowly


def print_fast(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.0005, 0.0001))
    print("\n")
    #prints text letter-by-letter quickly


def print_very_fast(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.000005, 0.000001))
    print("\n")
    #prints text letter-by-letter REALLY quickly


def death_screen():
    print_fast(ASCII.death_screen)
    exit()
    #Death screen


def standard_combat(target_name, target_health, target_damage, range, healing):
    print_slow("THREAT DETECTED")
    print(f"{target_name} APPROACHES")
    print(f"{Player.name} ATTACKS FIRST")
    Wait.wait(1)
    combat_loop = True
    weapon_loop = True

    while combat_loop == True:
        #Puts you into a loop until you either lose or win
        print(f"{target_name} HAS {target_health} HP")
        Wait.wait(1)

        while weapon_loop == True:
            #puts you in a loop until you pick a valid weapon
            print(f"""WEAPON CHOICES:
1 - {Weapons.Revolver.Name} - {Weapons.Revolver.Info}
2 - {Weapons.Shotgun.Name} - {Weapons.Shotgun.Info}
3 - {Weapons.Chaingun.Name} - {Weapons.Chaingun.Info}""")
            weapon_choice = str(input("Choice: ")).lower()
            alt_fire = input("Use the alternate firing option? "
                             "(Yes/No): ").lower()

            if "y" in alt_fire:
                if "1" in weapon_choice:
                    target_health = target_health - \
                        int(Weapons.Revolver.Damage) * 2
                    Player.current_health = Player.current_health - 10
                    #If the weapon selected is equal to 1 AND the range
                    #is greater than or equal to the enemies range value,
                    #you attack
                    weapon_loop = False

                elif "2" in weapon_choice:
                    target_health = target_health - \
                        int(Weapons.Shotgun.Damage) * 1.5
                    Player.current_health = Player.current_health - 50
                    #If the weapon selected is equal to 2 you shoot an infinite range
                    #shotgun projectile and take 50 damage
                    weapon_loop = False

            elif "n" in alt_fire:
                if "1" in weapon_choice and range <= Weapons.Revolver.Range:
                    target_health = target_health - \
                        int(Weapons.Revolver.Damage)
                    #If the weapon selected is equal to 1 AND the range is
                    #greater than or equal to the enemies range value,
                    #you attack
                    weapon_loop = False

                elif "2" in weapon_choice and range <= Weapons.Shotgun.Range:
                    target_health = target_health - \
                        int(Weapons.Shotgun.Damage)
                    #If the weapon selected is equal to 2 AND the range
                    #is greater than or equal to the enemies range value,
                    #you attack
                    weapon_loop = False

                elif "3" in weapon_choice and range <= Weapons.Chaingun.Range and Weapons.chaingun_used == False:
                    target_health = target_health - int(Weapons.Chaingun.Damage)
                    #If the weapon selected is equal to 3 AND the range is
                    #greater than or equal to the enemies range value AND the
                    #chaingun is functional, you attack
                    print("CHAINGUN USED, IT CANNOT BE USED AGAIN "
                          "UNTIL REPAIRED")
                    print("\n")
                    Weapons.chaingun_used = True
                    weapon_loop = False

                elif "3" in weapon_choice and Weapons.chaingun_used == True:
                    print("THE CHAINGUN HAS ALREADY BEEN USED. "
                          "YOU CANNOT USE IT AGAIN UNTIL YOU REPAIR IT.")
                    print("\n")
                    #prevents the chaingun from being used if it has already
                    #been used previously

                else:
                    print("PLEASE CHOOSE A VALID WEAPON WITH A SUITABLE RANGE."
                         " PICK THE NUMBER RELATED TO THE WEAPON.")
                    print("\n")
                    #In case the user enters a weapon that doesnt exist

            else:
                print("WEAPON HAS NO ALT FIRE/INVALID WEAPON")
                print("\n")
                Wait.wait(1)

        weapon_loop = True
        #sets weapon loop back to true so the next turn will work
        if Player.current_health <= 0:
            combat_loop = False
            print(f"{Player.name} HAS RAN OUT OF FUEL.")
            print("\n")
            Wait.wait(2)
            death_screen()
            Wait.wait(1)
            #Death :(

        elif target_health > 0:
            print(f"{target_name} HAS {target_health} HP")
            Wait.wait(1)
            #Tells the player how much health the enemy has
            print(f"{target_name} ATTACKS!")
            print("\n")
            Wait.wait(1)
            print(f"{target_name} HITS AND CAUSES {Player.name} TO LOSE "
                  f"{target_damage} FUEL.")
            Wait.wait(1)
            Player.current_health = Player.current_health - target_damage
            print(f"{Player.name} HAS {Player.current_health} FUEL REMAINING.")
            Wait.wait(1)
            if Player.current_health <= 0:
                combat_loop = False
                print(f"{Player.name} HAS RAN OUT OF FUEL.")
                print("\n")
                Wait.wait(2)
                death_screen()
                Wait.wait(1)
                #Death :(

        elif target_health <= 0:
            print(f"{target_name} HAS DIED")
            print("\n")
            Wait.wait(2)
            Player.current_health = Player.current_health + healing
            Player.HealthCheck()
            print(f"{Player.name} HAS {Player.current_health} FUEL REMAINING.")
            Wait.wait(2)
            combat_loop = False
            print(f"{Player.name} WINS.")
            print("\n")
            Wait.wait(1)
            #Victory!!! combat ends and the player heals,
            #determined by the enemies healing factor.

        else:
            print("ERROR")
            exit()
            #debug message