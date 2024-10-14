#Enemies
#Standard Enemies
class Enemy:
    def __init__(Self, Name, Health, Damage, Range, Healing, Class, Terminal):
        #All the values each enemy can have
        Self.Name = Name
        Self.Health = Health
        Self.Damage = Damage
        Self.Range = Range
        Self.Healing = Healing
        Self.Terminal = Terminal

#Bosses
class Boss:
    def __init__(Self, Name, Health, Class, Terminal):
        Self.Name = Name
        Self.Health = Health
        Self.Class = Class
        Self.Terminal = Terminal

#Standard Enemies

Filth = Enemy("Filth",
              10,
              20,
              1,
              15,
              "Lesser Husk",
              r"""A weak soul that was not powerful 
enough in life to even form a full body in hell. 
It does not think and only sprints towards what it 
percieves as food and attacks it.""")

Stray = Enemy("Stray",
              25,
              25,
              20,
              30,
              "Husk",
              r"""A soul that was strong enough in 
life to form a full ,albeit weak, body in hell. 
It is capible of basic thought and throws projectiles 
towards its enemies while running away, making the shotgun 
useless against it.""")

Schism = Enemy("Schism",
               50,
               25,
               15,
               50,
               "Husk",
               r"""A rare occourance where two 
Strays attempt to form in the same place,
causing this husk to form. It fires a barrage
of projectiles but not more than one are able to 
hit a small target, like yourself. it does not 
run as far as a Stray can as isn't very agile.""")

Crawler = Enemy("Crawler",
                30,
                30,
                5,
                40,
                "Lesser Demon",
                r"""A small, spider-like demon that was not
given enough hell mass for their shell, meaning that it has to get close
to its enemies to cause any major damage as it is not strong enough to
channel hell energy for ranged attacks.""")

Guardian = Enemy("Guardian",
                 75,
                 30,
                 5,
                 50,
                 "Demon",
                 r"""A large, stone statue animated by hell mass that
managed to breach the outside of the statue and 
force it to move.
It's movement is sluggish so it is incapible of
attacking from afar, as it cannot move its limbs
fast enough to throw any projectiles.""")

Shade = Enemy("Shade",
              100,
              35,
              5,
              30,
              "Puppet",
              r"""A small, humanoid creature comprised from the materials that 
are present in its enviroment. It is directly controlled by hell
and manifests in areas deemed as a 'background' by hell, they 
are used to ward off any unwanted visitors to these areas that 
are not meant to be interacted with.""")

Mimic = Enemy("Mimic",
              "",
              "",
              "",
              "",
              "Demon",
              """A demon that has no solid form, it mimics objects in its
enviroment in an attempt to trick its prey into a false
sense of security. 

It has no solid stats and they depend on what object it
is mimicing. Larger objects will result in a stronger
mimic while smaller objects will result in a weaker
mimic.""")

Colossus = Enemy("Colossus",
                 200,
                 50,
                 1,
                 150,
                 "Greater Husk",
                 r"""An incredibly powerful 
husk that is formed when someone with a very strong soul 
forms in hell. This enemy has a full awareness of their 
surroundings and attacks quickly and violently close to 
their opponents. They fight to ensure that hell does not 
become bored with them""")

#Bosses

Hijacked_1 = Boss("Hijacked",
                 2000,
                 "Supreme Machine/Demon",
                 r"""A damaged suit that was reanimated using hell mass.
The old pilot is still inside being puppeted by hell energy
and is forced by hell to pilot the reanimated suit.

This opponent is incredibly powerful and can kill its foes
in a matter of seconds if appropriate caution is not taken.
                 
DO NOT APPROACH WITHOUT A MAJOR POWER BOOST.
THE DEFAULT SUIT IS NOT ENOUGH TO DEFEAT IT.""")

#misc

SomethingWicked = Enemy("Something Wicked",
                        99999999,
                        99999999,
                        1,
                        1,
                        "????",
                        r"????")
Goose = Enemy("Goose",
              10000,
              15,
              1,
              1000,
              "Supreme Demon",
              r"""An unholy creature comprised of pure hatred and compressed
hell energy and hell mass. Nobody has managed to survive an encounter with it.

It takes pride in hunting its foes and will slowly chip away at its foes as it
enjoys the hunt.

Do not fight at all costs.
""")
#gag enemy

#All the enemies in the game