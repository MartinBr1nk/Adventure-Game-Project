#Imports
import time
import random
import Introduction
import Player
import Enemies

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
        time.sleep(random.uniform(0.005, 0.001))
    print("\n")

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