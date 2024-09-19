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

Filth = Enemy("Filth", 10, 20, 1, 25, "A weak soul that was not powerful enough in life to even form a full body in hell. It does not think and only sprints towards what it percieves as food and attacks it.")
Stray = Enemy("Stray", 25, 25, 20, 50, "A soul that was strong enough in life to form a full ,albeit weak, body in hell. It is capible of basic thought and throws projectiles towards its enemies while running away, making the shotgun useless against it.")
Schism = Enemy("Schism", 50, 25, 15, 75,  "A rare occourance where two Strays attempt to form in the same place, causing this husk to form. It fires a barrage of projectiles but not more than one are able to hit a small target, like yourself. it does not run as far as a Stray can as isn't very agile.")

#All the enemies in the game