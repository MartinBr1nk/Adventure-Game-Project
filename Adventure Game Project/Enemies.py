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

Filth = Enemy("Filth", 10, 20, 1, 15, "A weak soul that was not powerful "
              "enough in life to even form a full body in hell. "
              "It does not think and only sprints towards what it "
              "percieves as food and attacks it.")

Stray = Enemy("Stray", 25, 25, 20, 30, "A soul that was strong enough in "
              "life to form a full ,albeit weak, body in hell. "
              "It is capible of basic thought and throws projectiles "
              "towards its enemies while running away, making the shotgun "
              "useless against it.")

Schism = Enemy("Schism", 50, 25, 15, 50,  "A rare occourance where two "
               "Strays attempt to form in the same place, "
               "causing this husk to form. It fires a barrage "
               "of projectiles but not more than one are able to "
               "hit a small target, like yourself. it does not "
               "run as far as a Stray can as isn't very agile.")

Colossus = Enemy("Colossus", 200, 50, 1, 150, "An incredibly powerful "
                 "husk that is formed when someone with a very strong soul "
                 "forms in hell. This enemy has a full awareness of their "
                 "surroundings and attacks quickly and violently close to "
                 "their opponents. They fight to ensure that hell does not "
                 "become bored with them")

SomethingWicked = Enemy("Something Wicked", 99999999, 99999999, 1, 1, "????")

#All the enemies in the game