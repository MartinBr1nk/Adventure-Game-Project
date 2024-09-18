#Playerdata
CurrentHealth = 500
MaxHealth = 500
def HealthCheck():
    global CurrentHealth
    if CurrentHealth > MaxHealth:
        CurrentHealth = MaxHealth
        #if the player has above the max hp, it sets itself to the max hp