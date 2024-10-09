from Adventure_Game_Project import death_screen
#Playerdata
name = ""
global current_health
current_health = 500
max_health = 500
#HP for normal combat

boss_fight_max_health = 2000
boss_fight_current_health = 2000
#HP for boss fight combat
def DeathCheck():
    if current_health >= 0:
        death_screen()

def HealthCheck():
    if current_health > max_health:
        current_health = max_health
        #if the player has above the max hp, it sets itself to the max hp

def PlayerBossHPCheck():
    global boss_fight_current_health
    if boss_fight_current_health > boss_fight_max_health:
        boss_fight_current_health = boss_fight_max_health
        #if the player has above the max hp, it sets itself to the max hp