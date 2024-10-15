import os
import Wait
import ASCII
import random
def clear_screen():
    for clear_x in range(50):
        print("\n")
        #"Clears" the screen by pushing everything else away


def goose_check():
    goose_message = ["NO GOOSE DETECTED!!!!!! >:(", "BRING BACK MY GOOSE",
                     "RETURN THEM!", "RETURN THE GOOSE!!", "my goose :(",
                     "What about the goose?", "CURSE YOU FOR TAKING MY GOOSE",
                     "You monster. You took the goose.", "GOOSE GOOSE GOOSE",
                     "In this world, its honk or be honked.", "HONK (angry)",
                     "HONK HONK HONK (but angrier)",
                     "And thy punishment... IS HONK",
                     "The gaggle will not take kindly to your actions.",
                     "HONKITY HONK HONK (with evil intent)",
                     "YOU HONKED.", "HONK HONK HONK HONK HONK",
                     "RELEASE THE GEESE", "BRING THEM BACK!!!",
                     "You wouldn't steal a goose."]
    path = './Goose.png'
    gcheck = os.path.isfile(path)
    if gcheck == False:
        while True:
            print(goose_message[random.randint(0, 19)])
            print(ASCII.the_goose)
            Wait.wait(1)
            print("\n")
    elif gcheck == True:
        print("GOOSE DETECTED!!!! :D")
        Wait.wait(0.2)
        clear_screen()
    #If the goose is NOT present then the program WILL NOT WORK.
    #DO NOT REMOVE THIS CODE. THE PROGRAM WILL NOT WORK WITHOUT IT.

def goosed():
    for x in range(20):
        os.startfile("Goose.png")
        print("YOU'VE BEEN GOOSED")
    os.startfile("text/goosed.txt")