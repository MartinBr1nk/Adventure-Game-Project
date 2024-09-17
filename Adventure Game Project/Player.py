#Playerdata
CurrentHealth = 500
MaxHealth = 500
def HealthCheck():
    global CurrentHealth
    if CurrentHealth > MaxHealth:
        CurrentHealth = MaxHealth