#Imports
import time
import random
from SaveData import *
from Introduction import *

#functions
def Save(ValueName, Value):
    f = open("SaveData.py", "a")
    f.write(str(ValueName) + " = " + str(Value) + "\n")
    f.close()
    #useless saving system, it doesnt really work for what I want but I'm leaving it in in case I need it later

RandomVal = random.randint(0, 500)
#Random Value generated at the start of every run that can cause special events to happen

GameLoop = True
while GameLoop == True:
    IntroSequence()
