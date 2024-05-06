import random


class Player:
    def __init__(self, crew1, fuel1, cargo1, law1, name1, progress1):
        self.crew = crew1
        self.fuel = fuel1
        self.cargo = cargo1
        self.law = law1
        self.name = name1
        self.progress = progress1


# controls neg space of stats - inverse
crew = 20
fuel = 20
cargo = 20
law = 20
progress = False
ships = ["Andromeda", "Argo", "Starbuster 5000", "Galaxy Devourer 4000"]
name = ships[random.randint(0, len(ships)-1)]
p1 = Player(crew, fuel, cargo, law, name, progress)
