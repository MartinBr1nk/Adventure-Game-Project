#Weapons
ChaingunUsed = False
class Weapon:
    def __init__(Self, Name, Damage, Range, Info, Terminal):
        Self.Name = Name
        Self.Damage = Damage
        Self.Range = Range
        Self.Info = Info
        Self.Terminal = Terminal

Revolver = Weapon("Revolver", 25, 9999999, "Medium Damage, Perfect Accuracy", "Terminal Placeholder")
Shotgun = Weapon("Shotgun", 75, 5, "High Damage, Horrific Accuracy (5 Meter range)", "Terminal Placeholder")
Chaingun = Weapon("Chaingun", 500, 200, "Incredibly High Damage, High Accuracy (200 Meter range), Can only be used ONCE until it breaks and needs a repair", "Terminal Placeholder")

#All the weapons that the player uses in the game