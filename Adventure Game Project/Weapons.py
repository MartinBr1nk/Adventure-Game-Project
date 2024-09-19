#Weapons
chaingun_used = False
class Weapon:
    def __init__(Self, Name, Damage, Range, Info, Terminal):
        Self.Name = Name
        Self.Damage = Damage
        Self.Range = Range
        Self.Info = Info
        Self.Terminal = Terminal

Revolver = Weapon("Revolver", 15, 9999999, "Low Damage, Perfect Accuracy", "A revolver that uses electromagnets to fire its bullets at incredible speeds.")
Shotgun = Weapon("Shotgun", 50, 5, "High Damage, Horrific Accuracy (5 Meter range)", "A shotgun that fires an array of metal shards at fast speeds, a single shard can only cause a single cut while many shards can tear apart enemies.")
Chaingun = Weapon("Chaingun", 500, 200, "Incredibly High Damage, High Accuracy (200 Meter range), Can only be used ONCE until it breaks and needs a repair", "An experimental weapon with an incredible fire rate. It is able to unload its entire magazine before breaking and needing a repair.")

#All the weapons that the player uses in the game