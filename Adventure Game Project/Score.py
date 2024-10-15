import os
import Player
from Weapons import chaingun_used
total_score = 0

def score_modify(amount) -> str:
    global total_score
    """
    Changes how much score the player has by the amount passed into the function.

    It can only take integers.
    """
    total_score += amount

def score_calculate_and_save() -> str:
    global total_score
    """
    Calculates the final score and appends the players name and total score to Scoreboard.txt
    """
    if chaingun_used:
        total_score += 500

    if os.path.exists("text/Scoreboard.txt") == False:
        f = open("text/Scoreboard.txt", "x")
        f.close()
        f = open("text/Scoreboard.txt", "w")
        f.write("SCOREBOARD: ")
        f.close()
    
    f = open("text/Scoreboard.txt", "a")
    f.write(f"\n{Player.name} - {total_score}")
    f.close()

def scoreboard_wipe() -> str:
    """
    Wipes the scoreboard.
    """
    os.remove("text/Scoreboard.txt")
    f = open("text/Scoreboard.txt", "x")
    f.close()
    f = open("text/Scoreboard.txt", "w")
    f.write("SCOREBOARD: ")
    f.close()