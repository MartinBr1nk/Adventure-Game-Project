import Wait
import Enemies
import random
from Goose import wikipedia
def clear_screen():
    for clear_x in range(50):
        print("\n")
        #"Clears" the screen by pushing everything else away

def print_goose(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.0005, 0.0001))
    print("\n")
    #prints text letter-by-letter quickly

def terminal():
    while True:
        terminal_choice = input(f"""List of enemies:
        {Enemies.Filth.Name}
        {Enemies.Stray.Name}
        {Enemies.Schism.Name}
        {Enemies.Crawler.Name}
        {Enemies.Guardian.Name}
        {Enemies.Shade.Name}
        {Enemies.Mimic.Name}
        {Enemies.Colossus.Name}
        {Enemies.Hijacked_1.Name}
        {Enemies.SomethingWicked.Name}
        {Enemies.Goose.Name}
        Type "Exit" when you are ready to leave
        What enemy do you want to search for?: 
        """).lower()
        clear_screen()

        if Enemies.Filth.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Filth.Name}
CLASS - {Enemies.Filth.Class}
HEALTH - {Enemies.Filth.Health}
DAMAGE - {Enemies.Filth.Damage}
EFFECTIVE RANGE - {Enemies.Filth.Range}
AMOUNT OF FUEL - {Enemies.Filth.Healing}

TERMINAL ENTRY:
'{Enemies.Filth.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Stray.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Stray.Name}
CLASS - {Enemies.Stray.Class}
HEALTH - {Enemies.Stray.Health}
DAMAGE - {Enemies.Stray.Damage}
EFFECTIVE RANGE - {Enemies.Stray.Range}
AMOUNT OF FUEL - {Enemies.Stray.Healing}

TERMINAL ENTRY:
'{Enemies.Stray.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Schism.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Schism.Name}
CLASS - {Enemies.Schism.Class}
HEALTH - {Enemies.Schism.Health}
DAMAGE - {Enemies.Schism.Damage}
EFFECTIVE RANGE - {Enemies.Schism.Range}
AMOUNT OF FUEL - {Enemies.Schism.Healing}

TERMINAL ENTRY:
'{Enemies.Schism.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Crawler.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Crawler.Name}
CLASS - {Enemies.Crawler.Class}
HEALTH - {Enemies.Crawler.Health}
DAMAGE - {Enemies.Crawler.Damage}
EFFECTIVE RANGE - {Enemies.Crawler.Range}
AMOUNT OF FUEL - {Enemies.Crawler.Healing}

TERMINAL ENTRY:
'{Enemies.Crawler.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Guardian.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Guardian.Name}
CLASS - {Enemies.Guardian.Class}
HEALTH - {Enemies.Guardian.Health}
DAMAGE - {Enemies.Guardian.Damage}
EFFECTIVE RANGE - {Enemies.Guardian.Range}
AMOUNT OF FUEL - {Enemies.Guardian.Healing}

TERMINAL ENTRY:
'{Enemies.Guardian.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Shade.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Shade.Name}
CLASS - {Enemies.Shade.Class}
HEALTH - {Enemies.Shade.Health}
DAMAGE - {Enemies.Shade.Damage}
EFFECTIVE RANGE - {Enemies.Shade.Range}
AMOUNT OF FUEL - {Enemies.Shade.Healing}

TERMINAL ENTRY:
'{Enemies.Shade.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Mimic.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Mimic.Name}
CLASS - {Enemies.Mimic.Class}
HEALTH - VARIED
DAMAGE - VARIED
EFFECTIVE RANGE - VARIED
AMOUNT OF FUEL - VARIED

TERMINAL ENTRY:
'{Enemies.Mimic.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Colossus.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Colossus.Name}
CLASS - {Enemies.Colossus.Class}
HEALTH - {Enemies.Colossus.Health}
DAMAGE - {Enemies.Colossus.Damage}
EFFECTIVE RANGE - {Enemies.Colossus.Range}
AMOUNT OF FUEL - {Enemies.Colossus.Healing}

TERMINAL ENTRY:
'{Enemies.Colossus.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Hijacked_1.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Hijacked_1.Name}
CLASS - {Enemies.Hijacked_1.Class}
HEALTH - {Enemies.Hijacked_1.Health}

TERMINAL ENTRY:
'{Enemies.Hijacked_1.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.SomethingWicked.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.SomethingWicked.Name}
CLASS - {Enemies.SomethingWicked.Class}
HEALTH - {Enemies.SomethingWicked.Health}
DAMAGE - {Enemies.SomethingWicked.Damage}
EFFECTIVE RANGE - {Enemies.SomethingWicked.Range}
AMOUNT OF FUEL - {Enemies.SomethingWicked.Healing}

TERMINAL ENTRY:
'{Enemies.SomethingWicked.Terminal}'
""")
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()

        elif Enemies.Goose.Name.lower() in terminal_choice:
            print(f"""NAME - {Enemies.Goose.Name}
CLASS - {Enemies.Goose.Class}
HEALTH - {Enemies.Goose.Health}
DAMAGE - {Enemies.Goose.Damage}
EFFECTIVE RANGE - {Enemies.Goose.Range}
AMOUNT OF FUEL - {Enemies.Goose.Healing}

TERMINAL ENTRY:
""")
            print(r"LOADING 'https://en.wikipedia.org/wiki/Goose'...")
            Wait.wait(3)
            print_goose(wikipedia)
            #Shows the user all information to do with the enemy
            input("Press enter when you are ready to leave this entry.")
            clear_screen()
        elif "exit" in terminal_choice:
            break

        else:
            print("INVALID ENEMY")
