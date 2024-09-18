#Enemies
class Enemy:
    def __init__(Self, Name, Health, Damage, Range, Healing, Terminal):
        #All the values each enemy can have
        Self.Name = Name
        Self.Health = Health
        Self.Damage = Damage
        Self.Range = Range
        Self.Healing = Healing
        Self.Terminal = Terminal

Filth = Enemy("Filth", 10, 20, 1, 25, "Placeholder Terminal Entry")
Stray = Enemy("Stray", 25, 25, 20, 50, "Placeholder Terminal Entry")
Schism = Enemy("Schism", 50, 25, 15, 75,  "Placeholder Terminal Entry")

#All the enemies in the game