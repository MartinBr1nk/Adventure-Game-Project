import ASCII
import Wait
import random

#Playerdata
name = ""
global current_health
current_health = 500
max_health = 500
#HP for normal combat

boss_fight_max_health = 2000
boss_fight_current_health = 2000
#HP for boss fight combat

def print_fast(str):
    for letter in str:
        print(letter, end = ""),
        Wait.wait(random.uniform(0.0005, 0.0001))
    print("\n")
    #prints text letter-by-letter quickly

def death_screen():
    print_fast(ASCII.death_screen)
    exit()
    #Death screen

def HealthCheck():
    global current_health
    if current_health > max_health:
        current_health = max_health
        #if the player has above the max hp, it sets itself to the max hp

def DeathCheck():
    if current_health >= 0:
        death_screen()

def PlayerBossHPCheck():
    global boss_fight_current_health
    if boss_fight_current_health > boss_fight_max_health:
        boss_fight_current_health = boss_fight_max_health
        #if the player has above the max hp, it sets itself to the max hp