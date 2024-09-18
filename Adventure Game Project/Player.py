#Playerdata
current_health = 500
max_health = 500
def HealthCheck():
    global current_health
    if current_health > max_health:
        current_health = max_health
        #if the player has above the max hp, it sets itself to the max hp