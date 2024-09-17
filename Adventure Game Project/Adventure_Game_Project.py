#Imports
import time
import random
import Introduction

#functions
def Save(ValueName, Value):
    f = open("SaveData.py", "a")
    f.write(str(ValueName) + " = " + str(Value) + "\n")
    f.close()
    #useless saving system, it doesnt really work for what I want but I'm leaving it in in case I need it later

def CoolTyping(str):
    for letter in str:
        print(letter, end = ""),
        time.sleep(random.uniform(0.1, 0.05))
    print("\n")

RandomVal = random.randint(0, 500)
#Random Value generated at the start of every run that can cause special events to happen


GameLoop = True
while GameLoop == True:
    Introduction.IntroSequence()
    Name = Introduction.PlayerName
    