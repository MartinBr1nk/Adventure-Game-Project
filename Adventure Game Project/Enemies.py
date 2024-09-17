#Enemies
class Enemy:
    def __init__(Self, Name, Health, Damage, Terminal):
        Self.Name = Name
        Self.Health = Health
        Self.Damage = Damage
        Self.Terminal = Terminal

Filth = Enemy("Filth", 10, 20, "Placeholder Terminal Entry")
Stray = Enemy("Stray", 25, 25, "Placeholder Terminal Entry")
Schism = Enemy("Schism", 50, 25, "Placeholder Terminal Entry")