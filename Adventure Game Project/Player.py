#Playerdata
current_health = 1
max_health = 500
#HP for normal combat

boss_fight_max_health = 2000
boss_fight_current_health = 2000
#HP for boss fight combat
def HealthCheck():
    global current_health
    if current_health > max_health:
        current_health = max_health
        #if the player has above the max hp, it sets itself to the max hp

def PlayerBossHPCheck():
    global boss_fight_current_health
    if boss_fight_current_health > boss_fight_max_health:
        boss_fight_current_health = boss_fight_max_health
        #if the player has above the max hp, it sets itself to the max hp