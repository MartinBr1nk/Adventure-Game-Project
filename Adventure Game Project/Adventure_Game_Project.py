#Imports
import time
import random
from SaveData import *

#functions
def Save(ValueName, Value):
    f = open("SaveData.py", "a")
    f.write(str(ValueName) + " = " + str(Value) + "\n")
    f.close()

RandomVal = random.randint(0, 500)
print(RandomVal)
#Random Value generated at the start of every run that can cause special events to occour


if RanPreviously == False:
    PlayerName = input("Name the protagonist: ")
    if PlayerName == "":

        PlayerName = input("Enter a name, otherwise a default name will be chosen: ")
        if PlayerName == "":

            PlayerName = "Stanley"
            #this is a placeholder name, I'm not actually going to steal EVERY idea from the stanley parable
            print(f"Your name is {PlayerName}.")
            #Save("RanPreviously", "True")
            #Save("Name", PlayerName)

        else:
            print(f"Your name is {PlayerName}.")
            #Save("RanPreviously", "True")
            #Save("Name", PlayerName)

    else:
        print(f"Your name is {PlayerName}.")
        #Save("RanPreviously", "True")
        #Save("Name", PlayerName)

        